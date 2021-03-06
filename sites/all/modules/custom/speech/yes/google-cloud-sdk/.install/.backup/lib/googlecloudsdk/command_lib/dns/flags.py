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

"""Common flags for some of the DNS commands."""

from googlecloudsdk.calliope import base


def GetDnsZoneArg(help_text):
  return base.Argument(
      'dns_zone', metavar='ZONE_NAME',
      completion_resource='dns.managedZones',
      help=help_text)


def GetZoneArg(
    help_text='Name of the managed-zone whose record-sets you want to manage.'
):
  return base.Argument(
      '--zone',
      '-z',
      completion_resource='dns.managedZones',
      help=help_text,
      required=True)


def GetManagedZonesDnsNameArg():
  return base.Argument(
      '--dns-name',
      required=True,
      help='The DNS name suffix that will be managed with the created zone.')


def GetManagedZonesDescriptionArg(required=False):
  return base.Argument(
      '--description',
      required=required,
      help='Short description for the managed-zone.')


def AddCommonManagedZonesDnssecArgs(parser):
  """Add Common DNSSEC flags for the managed-zones group."""
  parser.add_argument(
      '--dnssec-state',
      choices={
          'off': 'Disable DNSSEC for the managed zone.',
          'on': 'Enable DNSSEC for the managed zone.',
          'transfer': 'Enable DNSSEC and allow transfering a signed zone in '
                      'or out.'},
      help='The DNSSEC state for this managed zone.')
  parser.add_argument(
      '--denial-of-existence',
      choices=['NSEC', 'NSEC3'],
      help='Requires DNSSEC enabled.')
  parser.add_argument(
      '--ksk-algorithm',
      help='String mnemonic specifying the DNSSEC algorithm of the '
           'key-signing key. Requires DNSSEC enabled. Example algorithms: '
           'RSASHA1, RSASHA256, RSASHA512, ECDSAP256SHA256, ECDSAP384SHA384')
  parser.add_argument(
      '--zsk-algorithm',
      help='String mnemonic specifying the DNSSEC algorithm of the '
           'zone-signing key. Requires DNSSEC enabled. Example algorithms: '
           'RSASHA1, RSASHA256, RSASHA512, ECDSAP256SHA256, ECDSAP384SHA384')
  parser.add_argument(
      '--ksk-key-length',
      type=int,
      help='Length of the key-signing key in bits. Requires DNSSEC enabled.')
  parser.add_argument(
      '--zsk-key-length',
      type=int,
      help='Length of the zone-signing key in bits. Requires DNSSEC enabled.')


CHANGES_FORMAT = 'table(id, startTime, status)'
