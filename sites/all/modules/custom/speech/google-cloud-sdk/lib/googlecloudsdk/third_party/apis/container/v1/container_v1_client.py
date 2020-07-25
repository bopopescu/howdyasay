"""Generated client library for container version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.container.v1 import container_v1_messages as messages


class ContainerV1(base_api.BaseApiClient):
  """Generated client library for service container version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://container.googleapis.com/'

  _PACKAGE = u'container'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform', u'https://www.googleapis.com/auth/userinfo.email']
  _VERSION = u'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'ContainerV1'
  _URL_VERSION = u'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new container handle."""
    url = url or self.BASE_URL
    super(ContainerV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.mainProjects_zones_signedUrls = self.MainProjectsZonesSignedUrlsService(self)
    self.mainProjects_zones_tokens = self.MainProjectsZonesTokensService(self)
    self.mainProjects_zones = self.MainProjectsZonesService(self)
    self.mainProjects = self.MainProjectsService(self)
    self.projects_zones_clusters_nodePools = self.ProjectsZonesClustersNodePoolsService(self)
    self.projects_zones_clusters = self.ProjectsZonesClustersService(self)
    self.projects_zones_operations = self.ProjectsZonesOperationsService(self)
    self.projects_zones = self.ProjectsZonesService(self)
    self.projects = self.ProjectsService(self)

  class MainProjectsZonesSignedUrlsService(base_api.BaseApiService):
    """Service class for the mainProjects_zones_signedUrls resource."""

    _NAME = u'mainProjects_zones_signedUrls'

    def __init__(self, client):
      super(ContainerV1.MainProjectsZonesSignedUrlsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates signed URLs that allow for writing a file to a private GCS bucket.
for storing backups of hosted main data. Signed URLs are explained here:
https://cloud.google.com/storage/docs/access-control#Signed-URLs

      Args:
        request: (ContainerMainProjectsZonesSignedUrlsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (SignedUrls) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.mainProjects.zones.signedUrls.create',
        ordered_params=[u'mainProjectId', u'zone'],
        path_params=[u'mainProjectId', u'zone'],
        query_params=[],
        relative_path=u'v1/mainProjects/{mainProjectId}/zones/{zone}/signedUrls',
        request_field=u'createSignedUrlsRequest',
        request_type_name=u'ContainerMainProjectsZonesSignedUrlsCreateRequest',
        response_type_name=u'SignedUrls',
        supports_download=False,
    )

  class MainProjectsZonesTokensService(base_api.BaseApiService):
    """Service class for the mainProjects_zones_tokens resource."""

    _NAME = u'mainProjects_zones_tokens'

    def __init__(self, client):
      super(ContainerV1.MainProjectsZonesTokensService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a compute-read-write (https://www.googleapis.com/auth/compute).
scoped OAuth2 access token for <project_number>, to allow a hosted main
to make modifications to its user's project.

      Args:
        request: (ContainerMainProjectsZonesTokensCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Token) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.mainProjects.zones.tokens.create',
        ordered_params=[u'mainProjectId', u'zone'],
        path_params=[u'mainProjectId', u'zone'],
        query_params=[],
        relative_path=u'v1/mainProjects/{mainProjectId}/zones/{zone}/tokens',
        request_field=u'createTokenRequest',
        request_type_name=u'ContainerMainProjectsZonesTokensCreateRequest',
        response_type_name=u'Token',
        supports_download=False,
    )

  class MainProjectsZonesService(base_api.BaseApiService):
    """Service class for the mainProjects_zones resource."""

    _NAME = u'mainProjects_zones'

    def __init__(self, client):
      super(ContainerV1.MainProjectsZonesService, self).__init__(client)
      self._upload_configs = {
          }

    def Authenticate(self, request, global_params=None):
      """Processes a request to authenticate a token. If it is able to authenticate.
the token, the email for the authorized user is also returned.
AuthenticateResponse also contains fields from the AuthenticateRequest. The
server is expected to only fill in the AuthenticateResponse.Status. This is
due to how the Authentication types are defined for the Kubernetes webhook
authenticator:
https://github.com/kubernetes/kubernetes/blob/master/pkg/apis/authentication.k8s.io/v1beta1/types.go.

      Args:
        request: (ContainerMainProjectsZonesAuthenticateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AuthenticateResponse) The response message.
      """
      config = self.GetMethodConfig('Authenticate')
      return self._RunMethod(
          config, request, global_params=global_params)

    Authenticate.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.mainProjects.zones.authenticate',
        ordered_params=[u'mainProjectId', u'zone', u'projectNumber', u'clusterId'],
        path_params=[u'clusterId', u'mainProjectId', u'projectNumber', u'zone'],
        query_params=[],
        relative_path=u'v1/mainProjects/{mainProjectId}/zones/{zone}/{projectNumber}/{clusterId}/authenticate',
        request_field=u'authenticateRequest',
        request_type_name=u'ContainerMainProjectsZonesAuthenticateRequest',
        response_type_name=u'AuthenticateResponse',
        supports_download=False,
    )

    def Authorize(self, request, global_params=None):
      """Processes the attributes of a user request and determines whether or not.
to authorize the request. If unauthorized, a reason is also provided. The
AuthorizeResponse also contains fields from the AuthorizeRequest. The
server is expected to only fill in the AuthorizeResponse.Status. This is
due to how the Authorization types are defined for the Kubernetes webhook
authorizer:
https://github.com/kubernetes/kubernetes/blob/master/pkg/apis/authorization/v1beta1/types.go.

      Args:
        request: (ContainerMainProjectsZonesAuthorizeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AuthorizeResponse) The response message.
      """
      config = self.GetMethodConfig('Authorize')
      return self._RunMethod(
          config, request, global_params=global_params)

    Authorize.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.mainProjects.zones.authorize',
        ordered_params=[u'mainProjectId', u'zone', u'projectNumber', u'clusterId'],
        path_params=[u'clusterId', u'mainProjectId', u'projectNumber', u'zone'],
        query_params=[],
        relative_path=u'v1/mainProjects/{mainProjectId}/zones/{zone}/{projectNumber}/{clusterId}/authorize',
        request_field=u'authorizeRequest',
        request_type_name=u'ContainerMainProjectsZonesAuthorizeRequest',
        response_type_name=u'AuthorizeResponse',
        supports_download=False,
    )

    def Imagereview(self, request, global_params=None):
      """Processes a request to verify the container image. If unverified, a reason.
is also provided. The ImageReviewResponse also contains fields from the
ImageReviewRequest. The server is expected to only fill in the
ImageReviewResponse.Status. This is due to how the ImageReview types are
defined for the Kubernetes webhook image review:
https://github.com/kubernetes/kubernetes/blob/master/pkg/apis/imagepolicy/v1beta1/types.go.

      Args:
        request: (ContainerMainProjectsZonesImagereviewRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ImageReviewResponse) The response message.
      """
      config = self.GetMethodConfig('Imagereview')
      return self._RunMethod(
          config, request, global_params=global_params)

    Imagereview.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.mainProjects.zones.imagereview',
        ordered_params=[u'mainProjectId', u'zone', u'projectNumber', u'clusterId'],
        path_params=[u'clusterId', u'mainProjectId', u'projectNumber', u'zone'],
        query_params=[],
        relative_path=u'v1/mainProjects/{mainProjectId}/zones/{zone}/{projectNumber}/{clusterId}/imagereview',
        request_field=u'imageReviewRequest',
        request_type_name=u'ContainerMainProjectsZonesImagereviewRequest',
        response_type_name=u'ImageReviewResponse',
        supports_download=False,
    )

    def Signcertificate(self, request, global_params=None):
      """Signs a CertificateSigningRequest (CSR) with the cluster's certificate.
authority (CA).

      Args:
        request: (CertificateSigningRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CertificateSigningRequest) The response message.
      """
      config = self.GetMethodConfig('Signcertificate')
      return self._RunMethod(
          config, request, global_params=global_params)

    Signcertificate.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.mainProjects.zones.signcertificate',
        ordered_params=[u'mainProjectId', u'zone', u'projectNumber', u'clusterId'],
        path_params=[u'clusterId', u'mainProjectId', u'projectNumber', u'zone'],
        query_params=[],
        relative_path=u'v1/mainProjects/{mainProjectId}/zones/{zone}/{projectNumber}/{clusterId}/signcertificate',
        request_field='<request>',
        request_type_name=u'CertificateSigningRequest',
        response_type_name=u'CertificateSigningRequest',
        supports_download=False,
    )

  class MainProjectsService(base_api.BaseApiService):
    """Service class for the mainProjects resource."""

    _NAME = u'mainProjects'

    def __init__(self, client):
      super(ContainerV1.MainProjectsService, self).__init__(client)
      self._upload_configs = {
          }

  class ProjectsZonesClustersNodePoolsService(base_api.BaseApiService):
    """Service class for the projects_zones_clusters_nodePools resource."""

    _NAME = u'projects_zones_clusters_nodePools'

    def __init__(self, client):
      super(ContainerV1.ProjectsZonesClustersNodePoolsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a node pool for a cluster.

      Args:
        request: (ContainerProjectsZonesClustersNodePoolsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.projects.zones.clusters.nodePools.create',
        ordered_params=[u'projectId', u'zone', u'clusterId'],
        path_params=[u'clusterId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools',
        request_field=u'createNodePoolRequest',
        request_type_name=u'ContainerProjectsZonesClustersNodePoolsCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes a node pool from a cluster.

      Args:
        request: (ContainerProjectsZonesClustersNodePoolsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'container.projects.zones.clusters.nodePools.delete',
        ordered_params=[u'projectId', u'zone', u'clusterId', u'nodePoolId'],
        path_params=[u'clusterId', u'nodePoolId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}',
        request_field='',
        request_type_name=u'ContainerProjectsZonesClustersNodePoolsDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Retrieves the node pool requested.

      Args:
        request: (ContainerProjectsZonesClustersNodePoolsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (NodePool) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'container.projects.zones.clusters.nodePools.get',
        ordered_params=[u'projectId', u'zone', u'clusterId', u'nodePoolId'],
        path_params=[u'clusterId', u'nodePoolId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}',
        request_field='',
        request_type_name=u'ContainerProjectsZonesClustersNodePoolsGetRequest',
        response_type_name=u'NodePool',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists the node pools for a cluster.

      Args:
        request: (ContainerProjectsZonesClustersNodePoolsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListNodePoolsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'container.projects.zones.clusters.nodePools.list',
        ordered_params=[u'projectId', u'zone', u'clusterId'],
        path_params=[u'clusterId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools',
        request_field='',
        request_type_name=u'ContainerProjectsZonesClustersNodePoolsListRequest',
        response_type_name=u'ListNodePoolsResponse',
        supports_download=False,
    )

    def Rollback(self, request, global_params=None):
      """Roll back the previously Aborted or Failed NodePool upgrade.
This will be an no-op if the last upgrade successfully completed.

      Args:
        request: (ContainerProjectsZonesClustersNodePoolsRollbackRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Rollback')
      return self._RunMethod(
          config, request, global_params=global_params)

    Rollback.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.projects.zones.clusters.nodePools.rollback',
        ordered_params=[u'projectId', u'zone', u'clusterId', u'nodePoolId'],
        path_params=[u'clusterId', u'nodePoolId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}:rollback',
        request_field=u'rollbackNodePoolUpgradeRequest',
        request_type_name=u'ContainerProjectsZonesClustersNodePoolsRollbackRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def SetManagement(self, request, global_params=None):
      """Sets the NodeManagement options for a node pool.

      Args:
        request: (ContainerProjectsZonesClustersNodePoolsSetManagementRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('SetManagement')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetManagement.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.projects.zones.clusters.nodePools.setManagement',
        ordered_params=[u'projectId', u'zone', u'clusterId', u'nodePoolId'],
        path_params=[u'clusterId', u'nodePoolId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/nodePools/{nodePoolId}/setManagement',
        request_field=u'setNodePoolManagementRequest',
        request_type_name=u'ContainerProjectsZonesClustersNodePoolsSetManagementRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class ProjectsZonesClustersService(base_api.BaseApiService):
    """Service class for the projects_zones_clusters resource."""

    _NAME = u'projects_zones_clusters'

    def __init__(self, client):
      super(ContainerV1.ProjectsZonesClustersService, self).__init__(client)
      self._upload_configs = {
          }

    def CompleteIpRotation(self, request, global_params=None):
      """Completes main IP rotation.

      Args:
        request: (ContainerProjectsZonesClustersCompleteIpRotationRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('CompleteIpRotation')
      return self._RunMethod(
          config, request, global_params=global_params)

    CompleteIpRotation.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.projects.zones.clusters.completeIpRotation',
        ordered_params=[u'projectId', u'zone', u'clusterId'],
        path_params=[u'clusterId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}:completeIpRotation',
        request_field=u'completeIPRotationRequest',
        request_type_name=u'ContainerProjectsZonesClustersCompleteIpRotationRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      """Creates a cluster, consisting of the specified number and type of Google.
Compute Engine instances.

By default, the cluster is created in the project's
[default network](/compute/docs/networks-and-firewalls#networks).

One firewall is added for the cluster. After cluster creation,
the cluster creates routes for each node to allow the containers
on that node to communicate with all other instances in the
cluster.

Finally, an entry is added to the project's global metadata indicating
which CIDR range is being used by the cluster.

      Args:
        request: (ContainerProjectsZonesClustersCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.projects.zones.clusters.create',
        ordered_params=[u'projectId', u'zone'],
        path_params=[u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters',
        request_field=u'createClusterRequest',
        request_type_name=u'ContainerProjectsZonesClustersCreateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      """Deletes the cluster, including the Kubernetes endpoint and all worker.
nodes.

Firewalls and routes that were configured during cluster creation
are also deleted.

Other Google Compute Engine resources that might be in use by the cluster
(e.g. load balancer resources) will not be deleted if they weren't present
at the initial create time.

      Args:
        request: (ContainerProjectsZonesClustersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'DELETE',
        method_id=u'container.projects.zones.clusters.delete',
        ordered_params=[u'projectId', u'zone', u'clusterId'],
        path_params=[u'clusterId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}',
        request_field='',
        request_type_name=u'ContainerProjectsZonesClustersDeleteRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets the details of a specific cluster.

      Args:
        request: (ContainerProjectsZonesClustersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Cluster) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'container.projects.zones.clusters.get',
        ordered_params=[u'projectId', u'zone', u'clusterId'],
        path_params=[u'clusterId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}',
        request_field='',
        request_type_name=u'ContainerProjectsZonesClustersGetRequest',
        response_type_name=u'Cluster',
        supports_download=False,
    )

    def LegacyAbac(self, request, global_params=None):
      """Enables or disables the ABAC authorization mechanism on a cluster.

      Args:
        request: (ContainerProjectsZonesClustersLegacyAbacRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('LegacyAbac')
      return self._RunMethod(
          config, request, global_params=global_params)

    LegacyAbac.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.projects.zones.clusters.legacyAbac',
        ordered_params=[u'projectId', u'zone', u'clusterId'],
        path_params=[u'clusterId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/legacyAbac',
        request_field=u'setLegacyAbacRequest',
        request_type_name=u'ContainerProjectsZonesClustersLegacyAbacRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists all clusters owned by a project in either the specified zone or all.
zones.

      Args:
        request: (ContainerProjectsZonesClustersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListClustersResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'container.projects.zones.clusters.list',
        ordered_params=[u'projectId', u'zone'],
        path_params=[u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters',
        request_field='',
        request_type_name=u'ContainerProjectsZonesClustersListRequest',
        response_type_name=u'ListClustersResponse',
        supports_download=False,
    )

    def ResourceLabels(self, request, global_params=None):
      """Sets labels on a cluster.

      Args:
        request: (ContainerProjectsZonesClustersResourceLabelsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('ResourceLabels')
      return self._RunMethod(
          config, request, global_params=global_params)

    ResourceLabels.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.projects.zones.clusters.resourceLabels',
        ordered_params=[u'projectId', u'zone', u'clusterId'],
        path_params=[u'clusterId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}/resourceLabels',
        request_field=u'setLabelsRequest',
        request_type_name=u'ContainerProjectsZonesClustersResourceLabelsRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def SetMainAuth(self, request, global_params=None):
      """Used to set main auth materials. Currently supports :-.
Changing the admin password of a specific cluster.
This can be either via password generation or explicitly set the password.

      Args:
        request: (ContainerProjectsZonesClustersSetMainAuthRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('SetMainAuth')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetMainAuth.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.projects.zones.clusters.setMainAuth',
        ordered_params=[u'projectId', u'zone', u'clusterId'],
        path_params=[u'clusterId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}:setMainAuth',
        request_field=u'setMainAuthRequest',
        request_type_name=u'ContainerProjectsZonesClustersSetMainAuthRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def StartIpRotation(self, request, global_params=None):
      """Start main IP rotation.

      Args:
        request: (ContainerProjectsZonesClustersStartIpRotationRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('StartIpRotation')
      return self._RunMethod(
          config, request, global_params=global_params)

    StartIpRotation.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.projects.zones.clusters.startIpRotation',
        ordered_params=[u'projectId', u'zone', u'clusterId'],
        path_params=[u'clusterId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}:startIpRotation',
        request_field=u'startIPRotationRequest',
        request_type_name=u'ContainerProjectsZonesClustersStartIpRotationRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def Update(self, request, global_params=None):
      """Updates the settings of a specific cluster.

      Args:
        request: (ContainerProjectsZonesClustersUpdateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Update')
      return self._RunMethod(
          config, request, global_params=global_params)

    Update.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PUT',
        method_id=u'container.projects.zones.clusters.update',
        ordered_params=[u'projectId', u'zone', u'clusterId'],
        path_params=[u'clusterId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/clusters/{clusterId}',
        request_field=u'updateClusterRequest',
        request_type_name=u'ContainerProjectsZonesClustersUpdateRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

  class ProjectsZonesOperationsService(base_api.BaseApiService):
    """Service class for the projects_zones_operations resource."""

    _NAME = u'projects_zones_operations'

    def __init__(self, client):
      super(ContainerV1.ProjectsZonesOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      """Cancels the specified operation.

      Args:
        request: (ContainerProjectsZonesOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'container.projects.zones.operations.cancel',
        ordered_params=[u'projectId', u'zone', u'operationId'],
        path_params=[u'operationId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/operations/{operationId}:cancel',
        request_field=u'cancelOperationRequest',
        request_type_name=u'ContainerProjectsZonesOperationsCancelRequest',
        response_type_name=u'Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets the specified operation.

      Args:
        request: (ContainerProjectsZonesOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'container.projects.zones.operations.get',
        ordered_params=[u'projectId', u'zone', u'operationId'],
        path_params=[u'operationId', u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/operations/{operationId}',
        request_field='',
        request_type_name=u'ContainerProjectsZonesOperationsGetRequest',
        response_type_name=u'Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists all operations in a project in a specific zone or all zones.

      Args:
        request: (ContainerProjectsZonesOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'container.projects.zones.operations.list',
        ordered_params=[u'projectId', u'zone'],
        path_params=[u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/operations',
        request_field='',
        request_type_name=u'ContainerProjectsZonesOperationsListRequest',
        response_type_name=u'ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsZonesService(base_api.BaseApiService):
    """Service class for the projects_zones resource."""

    _NAME = u'projects_zones'

    def __init__(self, client):
      super(ContainerV1.ProjectsZonesService, self).__init__(client)
      self._upload_configs = {
          }

    def GetServerconfig(self, request, global_params=None):
      """Returns configuration info about the Container Engine service.

      Args:
        request: (ContainerProjectsZonesGetServerconfigRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ServerConfig) The response message.
      """
      config = self.GetMethodConfig('GetServerconfig')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetServerconfig.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'container.projects.zones.getServerconfig',
        ordered_params=[u'projectId', u'zone'],
        path_params=[u'projectId', u'zone'],
        query_params=[],
        relative_path=u'v1/projects/{projectId}/zones/{zone}/serverconfig',
        request_field='',
        request_type_name=u'ContainerProjectsZonesGetServerconfigRequest',
        response_type_name=u'ServerConfig',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(ContainerV1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
