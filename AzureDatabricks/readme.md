# Azure Data Factory Learnings 🚀

This repository contains my learning notes, project experiments, and practical implementations using Azure Data Factory.

## 🔍 Topics Covered
- Pipelines, Activities, Triggers
- Integration Runtime
- Linked Services and Datasets
- Data Flows
- Monitoring & Logging
- ADF + Azure Databricks
- Real-world project ideas
Connect to Azure Data Lake Storage
Step 1: Create a Microsoft Entra ID service principal
To use service principals to connect to Azure Data Lake Storage, an admin user must create a new Microsoft Entra ID application. If you already have a Microsoft Entra ID service principal available, skip ahead to Step 2: Create a client secret for your service principal.
To create a Microsoft Entra ID service principal, follow these instructions:
1.	Sign in to the Azure portal.
 Note
The portal to use is different depending on whether your Microsoft Entra ID application runs in the Azure public cloud or in a national or sovereign cloud. For more information, see National clouds.
2.	If you have access to multiple tenants, subscriptions, or directories, click the Directories + subscriptions (directory with filter) icon in the top menu to switch to the directory in which you want to provision the service principal.
3.	Search for and select <Microsoft Entra ID.
4.	In Manage, click App registrations > New registration.
5.	For Name, enter a name for the application.
6.	In the Supported account types section, select Accounts in this organizational directory only (Single tenant).
7.	Click Register.
Step 2: Create a client secret for your service principal
1.	In Manage, click Certificates & secrets.
2.	On the Client secrets tab, click New client secret.
 
3.	In the Add a client secret pane, for Description, enter a description for the client secret.
4.	For Expires, select an expiry time period for the client secret, and then click Add.
5.	Copy and store the client secret's Value in a secure place, as this client secret is the password for your application.
6.	On the application page's Overview page, in the Essentials section, copy the following values:
•	Application (client) ID
•	Directory (tenant) ID
Step 3: Grant the service principal access to Azure Data Lake Storage
You grant access to storage resources by assigning roles to your service principal. In this tutorial, you assign the Storage Blob Data Contributor to the service principal on your Azure Data Lake Storage account. You may need to assign other roles depending on specific requirements.
1.	In the Azure portal, go to the Storage accounts service.
2.	Select an Azure storage account to use.
3.	Click Access Control (IAM).
4.	Click + Add and select Add role assignment from the dropdown menu.
5.	Set the Select field to the Microsoft Entra ID application name that you created in step 1 and set Role to Storage Blob Data Contributor.
6.	Click Save.
Step 4: Add the client secret to Azure Key Vault
You can store the client secret from step 1 in Azure Key Vault.
1.	In the Azure portal, go to the Key vault service.
2.	Select an Azure Key Vault to use.
3.	On the Key Vault settings pages, select Secrets.
4.	Click on + Generate/Import.
5.	In Upload options, select Manual.
6.	For Name, enter a name for the secret. The secret name must be unique within a Key Vault.
7.	For Value, paste the Client Secret that you stored in Step 1.
8.	Click Create.
Step 5: Configure your Azure key vault instance for Azure Databricks
1.	In the Azure Portal, go to the Azure key vault instance.
a.	Under Settings, select the Access configuration tab.
b.	Set Permission model to Vault access policy.
 Note
Creating an Azure Key Vault-backed secret scope role grants the Get and List permissions to the application ID for the Azure Databricks service using key vault access policies. The Azure role-based access control permission model is not supported with Azure Databricks.
c.	Under Settings, select Networking.
d.	In Firewalls and virtual networks set Allow access from: to Allow public access from specific virtual networks and IP addresses.
Under Exception, check Allow trusted Microsoft services to bypass this firewall.
 Note
You can also set Allow access from: to Allow public access from all networks.
Scope name - dbutils.secrets.listScopes()
Databricks CLI - databricks secrets list-scopes
Provide scope name


Step 6: Create Azure Key Vault-backed secret scope in your Azure Databricks workspace
To reference the client secret stored in an Azure Key Vault, you can create a secret scope backed by Azure Key Vault in Azure Databricks.
1.	Go to https://<databricks-instance>#secrets/createScope. This URL is case sensitive; scope in createScope must be uppercase.
 
2.	Enter the name of the secret scope. Secret scope names are case insensitive.
3.	Use the Manage Principal dropdown menu to specify whether All Users have MANAGE permission for this secret scope or only the Creator of the secret scope (that is to say, you).
4.	Enter the DNS Name (for example, https://databrickskv.vault.azure.net/) and Resource ID, for example:
Copy
/subscriptions/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/resourcegroups/databricks-rg/providers/Microsoft.KeyVault/vaults/databricksKV
These properties are available from the *Settings > Properties tab of an Azure Key Vault in your Azure portal.
5.	Click the Create button.
Step 7: Connect to Azure Data Lake Storage using python
You can now securely access data in the Azure storage account using OAuth 2.0 with your Microsoft Entra ID application service principal for authentication from an Azure Databricks notebook.
1.	Navigate to your Azure Databricks workspace and create a new python notebook.
2.	Run the following python code, with the replacements below, to connect to Azure Data Lake Storage.
PythonCopy
service_credential = dbutils.secrets.get(scope="<scope>",key="<service-credential-key>")

spark.conf.set("fs.azure.account.auth.type.<storage-account>.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.<storage-account>.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.<storage-account>.dfs.core.windows.net", "<application-id>")
spark.conf.set("fs.azure.account.oauth2.client.secret.<storage-account>.dfs.core.windows.net", service_credential)
spark.conf.set("fs.azure.account.oauth2.client.endpoint.<storage-account>.dfs.core.windows.net", "https://login.microsoftonline.com/<directory-id>/oauth2/token")
Replace
•	<scope> with the secret scope name from step 5.
•	<service-credential-key> with the name of the key containing the client secret.
•	<storage-account> with the name of the Azure storage account.
•	<application-id> with the Application (client) ID for the Microsoft Entra ID application.
•	<directory-id> with the Directory (tenant) ID for the Microsoft Entra ID application.
You have now successfully connected your Azure Databricks workspace to your Azure Data Lake Storage account.
Grant your Azure Databricks workspace access to Azure Data Lake Storage
If you configure a firewall on Azure Data Lake Storage, you must configure network settings to allow your Azure Databricks workspace to connect to Azure Data Lake Storage. First, ensure that your Azure Databricks workspace is deployed in your own virtual network following Deploy Azure Databricks in your Azure virtual network (VNet injection). You can then configure either private endpoints or access from your virtual network to allow connections from your subnets to your Azure Data Lake Storage account.
If you are using serverless compute like serverless SQL warehouses, you must grant access from the serverless compute plane to Azure Data Lake Storage. See Serverless compute plane networking.
Grant access using private endpoints
You can use private endpoints for your Azure Data Lake Storage account to allow your Azure Databricks workspace to securely access data over a private link.
To create a private endpoint by using the Azure Portal, see Tutorial: Connect to a storage account using an Azure Private Endpoint. Ensure to create the private endpoint in the same virtual network that your Azure Databricks workspace is deployed in.
Grant access from your virtual network
Virtual Network service endpoints allow you to secure your critical Azure service resources to only your virtual networks. You can enable a service endpoint for Azure Storage within the VNet that you used for your Azure Databricks workspace.
For more information, including Azure CLI and PowerShell instructions, see Grant access from a virtual network.
1.	Log in to the Azure Portal, as a user with the Storage Account Contributor role on your Azure Data Lake Storage account.
2.	Navigate to your Azure Storage account, and go to the Networking tab.
3.	Check that you've selected to allow access from Selected virtual networks and IP addresses.
4.	Under Virtual networks, select Add existing virtual network.
5.	In the side panel, under Subscription, select the subscription that your virtual network is in.
6.	Under Virtual networks, select the virtual network that your Azure Databricks workspace is deployed in.
7.	Under Subnets, pick Select all.
8.	Click Enable.
9.	Select Save to apply your changes.
