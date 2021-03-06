# Copyright 2016 Google Inc. All Rights Reserved.
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
"""ml-engine jobs cancel command."""
from googlecloudsdk.api_lib.ml_engine import jobs
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.ml_engine import flags
from googlecloudsdk.command_lib.ml_engine import jobs_util


def _AddCancelArgs(parser):
  flags.JOB_NAME.AddToParser(parser)


@base.ReleaseTracks(base.ReleaseTrack.BETA, base.ReleaseTrack.ALPHA)
class CancelBeta(base.SilentCommand):
  """Cancel a running Cloud ML Engine job."""

  @staticmethod
  def Args(parser):
    _AddCancelArgs(parser)

  def Run(self, args):
    return jobs_util.Cancel(jobs.JobsClient('v1beta1'), args.job)


@base.ReleaseTracks(base.ReleaseTrack.GA)
class CancelGa(base.SilentCommand):
  """Cancel a running Cloud ML Engine job."""

  @staticmethod
  def Args(parser):
    _AddCancelArgs(parser)

  def Run(self, args):
    return jobs_util.Cancel(jobs.JobsClient('v1'), args.job)


_DETAILED_HELP = {
    'DESCRIPTION': """\
*{command}* cancels a running Cloud ML Engine job. If the job is already
finished, the command will not perform an operation and exit successfully.
"""
}


CancelGa.detailed_help = _DETAILED_HELP
CancelBeta.detailed_help = _DETAILED_HELP
