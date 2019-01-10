# =========================================================================
# Copyright 2012-present Yunify, Inc.
# -------------------------------------------------------------------------
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this work except in compliance with the License.
# You may obtain a copy of the License in the LICENSE file, or at:
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========================================================================

########## API Actions ##########

# Access Key
ACTION_DESCRIBE_ACCESS_KEYS = "DescribeAccessKeys"

# Notification Center
ACTION_DESCRIBE_NOTIFICATION_CENTER_USER_POSTS = "DescribeNotificationCenterUserPosts"
ACTION_CREATE_NOTIFICATION_LIST = "CreateNotificationList"
ACTION_DESCRIBE_NOTIFICATION_LISTS = "DescribeNotificationLists"
ACTION_MODIFY_NOTIFICATION_LIST_ATTRIBUTES = "ModifyNotificationListAttributes"
ACTION_DELETE_NOTIFICATION_LISTS = "DeleteNotificationLists"
ACTION_CREATE_NOTIFICATION_ITEMS = "CreateNotificationItems"
ACTION_DESCRIBE_NOTIFICATION_ITEMS = "DescribeNotificationItems"
ACTION_DELETE_NOTIFICATION_ITEMS = "DeleteNotificationItems"
ACTION_VERIFY_NOTIFICATION_ITEM = "VerifyNotificationItem"

# zones
ACTION_DESCRIBE_ZONES = "DescribeZones"

# jobs
ACTION_DESCRIBE_JOBS = "DescribeJobs"

# images
ACTION_DESCRIBE_IMAGES = "DescribeImages"
ACTION_CAPTURE_INSTANCE = "CaptureInstance"
ACTION_DELETE_IMAGES = "DeleteImages"
ACTION_CEASE_IMAGES = "CeaseImages"
ACTION_MODIFY_IMAGE_ATTRIBUTES = "ModifyImageAttributes"

# instances
ACTION_DESCRIBE_INSTANCES = "DescribeInstances"
ACTION_RUN_INSTANCES = "RunInstances"
ACTION_RUN_INSTANCES_BY_CONFIGURATION = "RunInstancesByConfiguration"
ACTION_TERMINATE_INSTANCES = "TerminateInstances"
ACTION_CEASE_INSTANCES = "CeaseInstances"
ACTION_START_INSTANCES = "StartInstances"
ACTION_RESTART_INSTANCES = "RestartInstances"
ACTION_STOP_INSTANCES = "StopInstances"
ACTION_RESIZE_INSTANCES = "ResizeInstances"
ACTION_RESET_INSTANCES = "ResetInstances"
ACTION_MODIFY_INSTANCE_ATTRIBUTES = "ModifyInstanceAttributes"

# user data
ACTION_UPLOAD_USERDATA_ATTACHMENT = "UploadUserDataAttachment"

# volumes
ACTION_DESCRIBE_VOLUMES = "DescribeVolumes"
ACTION_CREATE_VOLUMES = "CreateVolumes"
ACTION_DELETE_VOLUMES = "DeleteVolumes"
ACTION_CEASE_VOLUMES = "CeaseVolumes"
ACTION_ATTACH_VOLUMES = "AttachVolumes"
ACTION_DETACH_VOLUMES = "DetachVolumes"
ACTION_RESIZE_VOLUMES = "ResizeVolumes"
ACTION_MODIFY_VOLUME_ATTRIBUTES = "ModifyVolumeAttributes"

# key pair
ACTION_DESCRIBE_KEY_PAIRS = "DescribeKeyPairs"
ACTION_CREATE_KEY_PAIR = "CreateKeyPair"
ACTION_DELETE_KEY_PAIRS = "DeleteKeyPairs"
ACTION_ATTACH_KEY_PAIRS = "AttachKeyPairs"
ACTION_DETACH_KEY_PAIRS = "DetachKeyPairs"
ACTION_MODIFY_KEYPAIR_ATTRIBUTES = "ModifyKeyPairAttributes"

# security group
ACTION_DESCRIBE_SECURITY_GROUPS = "DescribeSecurityGroups"
ACTION_CREATE_SECURITY_GROUP = "CreateSecurityGroup"
ACTION_MODIFY_SECURITY_GROUP_ATTRIBUTES = "ModifySecurityGroupAttributes"
ACTION_APPLY_SECURITY_GROUP = "ApplySecurityGroup"
ACTION_REMOVE_SECURITY_GROUP = "RemoveSecurityGroup"
ACTION_DELETE_SECURITY_GROUPS = "DeleteSecurityGroups"
ACTION_DESCRIBE_SECURITY_GROUP_RULES = "DescribeSecurityGroupRules"
ACTION_ADD_SECURITY_GROUP_RULES = "AddSecurityGroupRules"
ACTION_DELETE_SECURITY_GROUP_RULES = "DeleteSecurityGroupRules"
ACTION_MODIFY_SECURITY_GROUP_RULE_ATTRIBUTES = "ModifySecurityGroupRuleAttributes"
ACTION_DESCRIBE_SECURITY_GROUP_IPSETS = "DescribeSecurityGroupIPSets"
ACTION_CREATE_SECURITY_GROUP_IPSET = "CreateSecurityGroupIPSet"
ACTION_DELETE_SECURITY_GROUP_IPSETS = "DeleteSecurityGroupIPSets"
ACTION_MODIFY_SECURITY_GROUP_IPSET_ATTRIBUTES = "ModifySecurityGroupIPSetAttributes"

# vxnets
ACTION_DESCRIBE_VXNETS = "DescribeVxnets"
ACTION_CREATE_VXNETS = "CreateVxnets"
ACTION_DELETE_VXNETS = "DeleteVxnets"
ACTION_JOIN_VXNET = "JoinVxnet"
ACTION_LEAVE_VXNET = "LeaveVxnet"
ACTION_MODIFY_VXNET_ATTRIBUTES = "ModifyVxnetAttributes"
ACTION_DESCRIBE_VXNET_INSTANCES = "DescribeVxnetInstances"

# router
ACTION_CREATE_ROUTERS = "CreateRouters"
ACTION_UPDATE_ROUTERS = "UpdateRouters"
ACTION_DELETE_ROUTERS = "DeleteRouters"
ACTION_JOIN_ROUTER = "JoinRouter"
ACTION_LEAVE_ROUTER = "LeaveRouter"
ACTION_POWEROFF_ROUTERS = "PowerOffRouters"
ACTION_POWERON_ROUTERS = "PowerOnRouters"
ACTION_DESCRIBE_ROUTERS = "DescribeRouters"
ACTION_DESCRIBE_ROUTER_VXNETS = "DescribeRouterVxnets"
ACTION_MODIFY_ROUTER_ATTRIBUTES = "ModifyRouterAttributes"
ACTION_MODIFY_ROUTER_STATIC_ATTRIBUTES = "ModifyRouterStaticAttributes"
ACTION_DESCRIBE_ROUTER_STATICS = "DescribeRouterStatics"
ACTION_ADD_ROUTER_STATICS = "AddRouterStatics"
ACTION_DELETE_ROUTER_STATICS = "DeleteRouterStatics"
ACTION_MODIFY_ROUTER_STATIC_ENTRY_ATTRIBUTES = "ModifyRouterStaticEntryAttributes"
ACTION_DESCRIBE_ROUTER_STATIC_ENTRIES = "DescribeRouterStaticEntries"
ACTION_ADD_ROUTER_STATIC_ENTRIES = "AddRouterStaticEntries"
ACTION_DELETE_ROUTER_STATIC_ENTRIES = "DeleteRouterStaticEntries"

# eip
ACTION_ASSOCIATE_EIP = "AssociateEip"
ACTION_DISSOCIATE_EIPS = "DissociateEips"
ACTION_ALLOCATE_EIPS = "AllocateEips"
ACTION_RELEASE_EIPS = "ReleaseEips"
ACTION_DESCRIBE_EIPS = "DescribeEips"
ACTION_MODIFY_EIP_ATTRIBUTES = "ModifyEipAttributes"
ACTION_CHANGE_EIPS_BANDWIDTH = "ChangeEipsBandwidth"
ACTION_CHANGE_EIPS_BILLING_MODE = "ChangeEipsBillingMode"

# dns alias
ACTION_DESCRIBE_DNS_ALIASES = "DescribeDNSAliases"
ACTION_ASSOCIATE_DNS_ALIAS = "AssociateDNSAlias"
ACTION_DISSOCIATE_DNS_ALIASES = "DissociateDNSAliases"
ACTION_GET_DNS_LABEL = "GetDNSLabel"

# lb
ACTION_DESCRIBE_LOADBALANCERS = "DescribeLoadBalancers"
ACTION_CREATE_LOADBALANCER = "CreateLoadBalancer"
ACTION_DELETE_LOADBALANCERS = "DeleteLoadBalancers"
ACTION_ASSOCIATE_EIPS_TO_LOADBALANCER = "AssociateEipsToLoadBalancer"
ACTION_DISSOCIATE_EIPS_FROM_LOADBALANCER = "DissociateEipsFromLoadBalancer"
ACTION_UPDATE_LOADBALANCERS = "UpdateLoadBalancers"
ACTION_STOP_LOADBALANCERS = "StopLoadBalancers"
ACTION_START_LOADBALANCERS = "StartLoadBalancers"
ACTION_MODIFY_LOADBALANCER_ATTRIBUTES = "ModifyLoadBalancerAttributes"

ACTION_DESCRIBE_LOADBALANCER_LISTENERS = "DescribeLoadBalancerListeners"
ACTION_ADD_LOADBALANCER_LISTENERS = "AddLoadBalancerListeners"
ACTION_DELETE_LOADBALANCER_LISTENERS = "DeleteLoadBalancerListeners"
ACTION_MODIFY_LOADBALANCER_LISTENER_ATTRIBUTES = "ModifyLoadBalancerListenerAttributes"
ACTION_ADD_LOADBALANCER_BACKENDS = "AddLoadBalancerBackends"
ACTION_DELETE_LOADBALANCER_BACKENDS = "DeleteLoadBalancerBackends"
ACTION_MODIFY_LOADBALANCER_BACKEND_ATTRIBUTES = "ModifyLoadBalancerBackendAttributes"
ACTION_DESCRIBE_LOADBALANCER_BACKENDS = "DescribeLoadBalancerBackends"

ACTION_CREATE_LOADBALANCER_POLICY = "CreateLoadBalancerPolicy"
ACTION_MODIFY_LOADBALANCER_POLICY_ATTRIBUTES = "ModifyLoadBalancerPolicyAttributes"
ACTION_DESCRIBE_LOADBALANCER_POLICIES = "DescribeLoadBalancerPolicies"
ACTION_DELETE_LOADBALANCER_POLICIES = "DeleteLoadBalancerPolicies"
ACTION_APPLY_LOADBALANCER_POLICY = "ApplyLoadBalancerPolicy"

ACTION_DESCRIBE_LOADBALANCER_POLICY_RULES = "DescribeLoadBalancerPolicyRules"
ACTION_ADD_LOADBALANCER_POLICY_RULES = "AddLoadBalancerPolicyRules"
ACTION_MODIFY_LOADBALANCER_POLICY_RULE_ATTRIBUTES = "ModifyLoadBalancerPolicyRuleAttributes"
ACTION_DELETE_LOADBALANCER_POLICY_RULES = "DeleteLoadBalancerPolicyRules"

ACTION_CREATE_SERVER_CERTIFICATE = "CreateServerCertificate"
ACTION_DESCRIBE_SERVER_CERTIFICATES = "DescribeServerCertificates"
ACTION_MODIFY_SERVER_CERTIFICATE_ATTRIBUTES = "ModifyServerCertificateAttributes"
ACTION_DELETE_SERVER_CERTIFICATES = "DeleteServerCertificates"

# monitor
ACTION_GET_MONITOR = "GetMonitor"
ACTION_GET_LOADBALANCER_MONITOR = "GetLoadBalancerMonitor"

# snapshot
ACTION_CREATE_SNAPSHOTS = "CreateSnapshots"
ACTION_DELETE_SNAPSHOTS = "DeleteSnapshots"
ACTION_APPLY_SNAPSHOTS = "ApplySnapshots"
ACTION_DESCRIBE_SNAPSHOTS = "DescribeSnapshots"
ACTION_MODIFY_SNAPSHOT_ATTRIBUTES = "ModifySnapshotAttributes"
ACTION_CAPTURE_INSTANCE_FROM_SNAPSHOT = "CaptureInstanceFromSnapshot"
ACTION_CREATE_VOLUME_FROM_SNAPSHOT = "CreateVolumeFromSnapshot"

# rdb
ACTION_DESCRIBE_RDBS = "DescribeRDBs"
ACTION_CREATE_RDB = "CreateRDB"
ACTION_RESIZE_RDBS = "ResizeRDBs"
ACTION_START_RDBS = "StartRDBs"
ACTION_STOP_RDBS = "StopRDBs"

# mongo
ACTION_DESCRIBE_MONGOS = "DescribeMongos"
ACTION_RESIZE_MONGOS = "ResizeMongos"
ACTION_START_MONGOS = "StartMongos"
ACTION_STOP_MONGOS = "StopMongos"

# cache
ACTION_DESCRIBE_CACHES = "DescribeCaches"
ACTION_CREATE_CACHE = "CreateCache"
ACTION_RESIZE_CACHES = "ResizeCaches"
ACTION_START_CACHES = "StartCaches"
ACTION_STOP_CACHES = "StopCaches"

# spark
ACTION_DESCRIBE_SPARKS = "DescribeSparks"
ACTION_START_SPARKS = "StartSparks"
ACTION_STOP_SPARKS = "StopSparks"
ACTION_ADD_SPARK_NODES = "AddSparkNodes"
ACTION_DELETE_SPARK_NODES = "DeleteSparkNodes"
ACTION_CREATE_SPARK = "CreateSpark"
ACTION_DELETE_SPARKS = "DeleteSparks"

# hadoop
ACTION_DESCRIBE_HADOOPS = "DescribeHadoops"
ACTION_START_HADOOPS = "StartHadoops"
ACTION_STOP_HADOOPS = "StopHadoops"
ACTION_ADD_HADOOP_NODES = "AddHadoopNodes"
ACTION_DELETE_HADOOP_NODES = "DeleteHadoopNodes"
ACTION_CREATE_HADOOP = "CreateHadoop"
ACTION_DELETE_HADOOPS = "DeleteHadoops"

# zk
ACTION_DESCRIBE_ZOOKEEPERS = "DescribeZookeepers"
ACTION_START_ZOOKEEPERS = "StartZookeepers"
ACTION_STOP_ZOOKEEPERS = "StopZookeepers"

# elasticsearch
ACTION_DESCRIBE_ELASTICSEARCHS = "DescribeElasticsearchs"
ACTION_START_ELASTICSEARCHS = "StartElasticsearchs"
ACTION_STOP_ELASTICSEARCHS = "StopElasticsearchs"

# queue
ACTION_DESCRIBE_QUEUES = "DescribeQueues"
ACTION_START_QUEUES = "StartQueues"
ACTION_STOP_QUEUES = "StopQueues"

# tag
ACTION_DESCRIBE_TAGS = "DescribeTags"
ACTION_CREATE_TAG = "CreateTag"
ACTION_DELETE_TAGS = "DeleteTags"
ACTION_MODIFY_TAG_ATTRIBUTES = "ModifyTagAttributes"
ACTION_ATTACH_TAGS = "AttachTags"
ACTION_DETACH_TAGS = "DetachTags"

# nic
ACTION_DESCRIBE_NICS = "DescribeNics"
ACTION_CREATE_NICS = "CreateNics"
ACTION_ATTACH_NICS = "AttachNics"
ACTION_DETACH_NICS = "DetachNics"
ACTION_MODIFY_NIC_ATTRIBUTES = "ModifyNicAttributes"
ACTION_DELETE_NICS = "DeleteNics"

# S2
ACTION_CREATE_S2_SERVER = "CreateS2Server"
ACTION_DESCRIBE_S2_SERVERS = "DescribeS2Servers"
ACTION_MODIFY_S2_SERVER = "ModifyS2ServerAttributes"
ACTION_RESIZE_S2_SERVERS = "ResizeS2Servers"
ACTION_DELETE_S2_SERVERS = "DeleteS2Servers"
ACTION_POWERON_S2_SERVERS = "PowerOnS2Servers"
ACTION_POWEROFF_S2_SERVERS = "PowerOffS2Servers"
ACTION_UPDATE_S2_SERVERS = "UpdateS2Servers"
ACTION_CHANGE_S2_SERVER_VXNET = "ChangeS2ServerVxnet"
ACTION_CREATE_S2_SHARED_TARGET = "CreateS2SharedTarget"
ACTION_DESCRIBE_S2_SHARED_TARGETS = "DescribeS2SharedTargets"
ACTION_DELETE_S2_SHARED_TARGETS = "DeleteS2SharedTargets"
ACTION_ENABLE_S2_SHARED_TARGETS = "EnableS2SharedTargets"
ACTION_DISABLE_S2_SHARED_TARGETS = "DisableS2SharedTargets"
ACTION_MODIFY_S2_SHARED_TARGET = "ModifyS2SharedTargetAttributes"
ACTION_ATTACH_TO_S2_SHARED_TARGET = "AttachToS2SharedTarget"
ACTION_DETACH_FROM_S2_SHARED_TARGET = "DetachFromS2SharedTarget"
ACTION_DESCRIBE_S2_DEFAULT_PARAMETERS = "DescribeS2DefaultParameters"
ACTION_CREATE_S2_GROUP = "CreateS2Group"
ACTION_DESCRIBE_S2_GROUPS = "DescribeS2Groups"
ACTION_MODIFY_S2_GROUP = "ModifyS2Group"
ACTION_DELETE_S2_GROUPS = "DeleteS2Groups"
ACTION_CREATE_S2_ACCOUNT = "CreateS2Account"
ACTION_DESCRIBE_S2_ACCOUNTS = "DescribeS2Accounts"
ACTION_MODIFY_S2_ACCOUNT = "ModifyS2Account"
ACTION_DELETE_S2_ACCOUNTS = "DeleteS2Accounts"
ACTION_ASSOCIATE_S2_ACCOUNT_GROUP = "AssociateS2AccountGroup"
ACTION_DISSOCIATE_S2_ACCOUNT_GROUP = "DissociateS2AccountGroup"

# Alarm
ACTION_DESCRIBE_ALARM_POLICIES = "DescribeAlarmPolicies"
ACTION_CREATE_ALARM_POLICY = "CreateAlarmPolicy"
ACTION_MODIFY_ALARM_POLICY_ATTRIBUTES = "ModifyAlarmPolicyAttributes"
ACTION_DELETE_ALARM_POLICIES = "DeleteAlarmPolicies"
ACTION_DESCRIBE_ALARM_POLICY_RULES = "DescribeAlarmPolicyRules"
ACTION_ADD_ALARM_POLICY_RULES = "AddAlarmPolicyRules"
ACTION_MODIFY_ALARM_POLICY_RULE_ATTRIBUTES = "ModifyAlarmPolicyRuleAttributes"
ACTION_DELETE_ALARM_POLICY_RULES = "DeleteAlarmPolicyRules"
ACTION_DESCRIBE_ALARM_POLICY_ACTIONS = "DescribeAlarmPolicyActions"
ACTION_ADD_ALARM_POLICY_ACTIONS = "AddAlarmPolicyActions"
ACTION_MODIFY_ALARM_POLICY_ACTION_ATTRIBUTES = "ModifyAlarmPolicyActionAttributes"
ACTION_DELETE_ALARM_POLICY_ACTIONS = "DeleteAlarmPolicyActions"
ACTION_ASSOCIATE_ALARM_POLICY = "AssociateAlarmPolicy"
ACTION_DISSOCIATE_ALARM_POLICY = "DissociateAlarmPolicy"
ACTION_APPLY_ALARM_POLICY = "ApplyAlarmPolicy"
ACTION_DESCRIBE_ALARMS = "DescribeAlarms"
ACTION_DESCRIBE_ALARM_HISTORY = "DescribeAlarmHistory"

# Billing
ACTION_GET_BALANCE = "GetBalance"
ACTION_GET_LEASE_INFO = "GetLeaseInfo"

# Collaboration
ACTION_DESCRIBE_SHARED_RESOURCE_GROUPS = "DescribeSharedResourceGroups"
ACTION_DESCRIBE_RESOURCE_GROUPS = "DescribeResourceGroups"
ACTION_CREATE_RESOURCE_GROUPS = "CreateResourceGroups"
ACTION_MODIFY_RESOURCE_GROUP_ATTRIBUTES = "ModifyResourceGroupAttributes"
ACTION_DELETE_RESOURCE_GROUPS = "DeleteResourceGroups"
ACTION_DESCRIBE_RESOURCE_GROUP_ITEMS = "DescribeResourceGroupItems"
ACTION_ADD_RESOURCE_GROUP_ITEMS = "AddResourceGroupItems"
ACTION_DELETE_RESOURCE_GROUP_ITEMS = "DeleteResourceGroupItems"
ACTION_DESCRIBE_USER_GROUPS = "DescribeUserGroups"
ACTION_CREATE_USER_GROUPS = "CreateUserGroups"
ACTION_MODIFY_USER_GROUP_ATTRIBUTES = "ModifyUserGroupAttributes"
ACTION_DELETE_USER_GROUPS = "DeleteUserGroups"
ACTION_DESCRIBE_USER_GROUP_MEMBERS = "DescribeUserGroupMembers"
ACTION_ADD_USER_GROUP_MEMBERS = "AddUserGroupMembers"
ACTION_MODIFY_USER_GROUP_MEMBER_ATTRIBUTES = "ModifyUserGroupMemberAttributes"
ACTION_DELETE_USER_GROUP_MEMBERS = "DeleteUserGroupMembers"
ACTION_DESCRIBE_GROUP_ROLES = "DescribeGroupRoles"
ACTION_CREATE_GROUP_ROLES = "CreateGroupRoles"
ACTION_MODIFY_GROUP_ROLE_ATTRIBUTES = "ModifyGroupRoleAttributes"
ACTION_DELETE_GROUP_ROLES = "DeleteGroupRoles"
ACTION_DESCRIBE_GROUP_ROLE_RULES = "DescribeGroupRoleRules"
ACTION_ADD_GROUP_ROLE_RULES = "AddGroupRoleRules"
ACTION_MODIFY_GROUP_ROLE_RULE_ATTRIBUTES = "ModifyGroupRoleRuleAttributes"
ACTION_DELETE_GROUP_ROLE_RULES = "DeleteGroupRoleRules"
ACTION_GRANT_RESOURCE_GROUPS_TO_USER_GROUPS = "GrantResourceGroupsToUserGroups"
ACTION_REVOKE_RESOURCE_GROUPS_FROM_USER_GROUPS = "RevokeResourceGroupsFromUserGroups"
ACTION_DESCRIBE_RESOURCE_USER_GROUPS = "DescribeResourceUserGroups"


########## Constants for resource ##########

# sg
DIRECTION_EGRESS = 1
DIRECTION_INGRESS = 0

# vxnet
VXNET_TYPE_MANAGED = 1
VXNET_TYPE_UNMANAGED = 0

# lb
BALANCE_ROUNDROBIN = "roundrobin"
BALANCE_LEASTCONN = "leastconn"
HEADER_X_FORWARD_FOR = 1
HEADER_QC_LBID = 2
HEADER_QC_LBIP = 4
LB_TYPE_MAXCONN_5k = 0
LB_TYPE_MAXCONN_20k = 1
LB_TYPE_MAXCONN_40k = 2
LB_TYPE_MAXCONN_100k = 3
LB_TYPE_MAXCONN_200k = 4
LB_TYPE_MAXCONN_500k = 5

# eip
EIP_BILLING_MODE_BANDWIDTH = "bandwidth"
EIP_BILLING_MODE_TRAFFIC = "traffic"

# cluster
ACTION_START_CLUSTERS = "StartClusters"
ACTION_STOP_CLUSTERS = "StopClusters"
ACTION_RESIZE_CLUSTER = "ResizeCluster"
ACTION_DESCRIBE_CLUSTERS = "DescribeClusters"
ACTION_ADD_CLUSTER_NODES = "AddClusterNodes"
ACTION_DELETE_CLUSTER_NODES = "DeleteClusterNodes"
ACTION_DELETE_CLUSTERS = "DeleteClusters"