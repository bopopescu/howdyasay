# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Command for labels update to instances."""

from googlecloudsdk.api_lib.compute import base_classes
from googlecloudsdk.api_lib.compute.operations import poller
from googlecloudsdk.api_lib.util import waiter
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.compute import flags
from googlecloudsdk.command_lib.compute.instances import flags as instances_flags
from googlecloudsdk.command_lib.util import labels_util


@base.ReleaseTracks(base.ReleaseTrack.ALPHA, base.ReleaseTrack.BETA)
class Update(base.UpdateCommand):
  r"""Update a Google Compute Engine virtual machine.

  *{command}* updates labels for a Google Compute Engine
  virtual machine.  For example:

    $ {command} example-instance --zone us-central1-a \
      --update-labels=k0=value1,k1=value2 --remove-labels=k3

  will add/update labels ``k0'' and ``k1'' and remove labels with key ``k3''.

  Labels can be used to identify the instance and to filter them as in

    $ {parent_command} list --filter='labels.k1:value2'

  To list existing labels

    $ {parent_command} describe example-instance --format='default(labels)'

  """

  @staticmethod
  def Args(parser):
    instances_flags.INSTANCE_ARG.AddArgument(parser)
    labels_util.AddUpdateLabelsFlags(parser)

  def Run(self, args):
    holder = base_classes.ComputeApiHolder(self.ReleaseTrack())
    client = holder.client.apitools_client
    messages = holder.client.messages

    instance_ref = instances_flags.INSTANCE_ARG.ResolveAsResource(
        args, holder.resources,
        scope_lister=flags.GetDefaultScopeLister(holder.client))

    update_labels, remove_labels = labels_util.GetAndValidateOpsFromArgs(args)

    instance = client.instances.Get(
        messages.ComputeInstancesGetRequest(**instance_ref.AsDict()))

    replacement = labels_util.UpdateLabels(
        instance.labels,
        messages.InstancesSetLabelsRequest.LabelsValue,
        update_labels=update_labels,
        remove_labels=remove_labels)

    if not replacement:
      return instance

    request = messages.ComputeInstancesSetLabelsRequest(
        project=instance_ref.project,
        instance=instance_ref.instance,
        zone=instance_ref.zone,
        instancesSetLabelsRequest=
        messages.InstancesSetLabelsRequest(
            labelFingerprint=instance.labelFingerprint,
            labels=replacement))

    operation = client.instances.SetLabels(request)
    operation_ref = holder.resources.Parse(
        operation.selfLink, collection='compute.zoneOperations')

    operation_poller = poller.Poller(client.instances)
    return waiter.WaitFor(
        operation_poller, operation_ref,
        'Updating labels of instance [{0}]'.format(
            instance_ref.Name()))