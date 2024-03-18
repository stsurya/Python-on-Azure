'''The follwoing script is working on my local machine but not via pipeline failing at line no:12 authentication'''


# Import the needed credential and management objects from the libraries.
import os
import variables

from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# Acquire a credential object using DevaultAzureCredential.
credential = DefaultAzureCredential()
print("credential=", credential)

# Retrieve subscription ID from environment variable.
subscription_id = variables.AZURE_SUBSCRIPTION_ID

# Obtain the management object for resources.
resource_client = ResourceManagementClient(credential, subscription_id)
print("resourceClient=", resource_client)

# # Provision the resource group.
# rg_result = resource_client.resource_groups.create_or_update(
#     variables.resourceGroupName, {"location": variables.location}
# )

# # Within the ResourceManagementClient is an object named resource_groups,
# # which is of class ResourceGroupsOperations, which contains methods like
# # create_or_update.
# #
# # The second parameter to create_or_update here is technically a ResourceGroup
# # object. You can create the object directly using ResourceGroup(location=
# # LOCATION) or you can express the object as inline JSON as shown here. For
# # details, see Inline JSON pattern for object arguments at
# # https://learn.microsoft.com/azure/developer/python/sdk
# # /azure-sdk-library-usage-patterns#inline-json-pattern-for-object-arguments

# print(
#     f"Provisioned resource group {rg_result.name} in the {rg_result.location} region"
# )
