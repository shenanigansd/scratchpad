param location string = resourceGroup().location

@minLength(3)
@maxLength(24)
param name string = 'testsadarbia'

@allowed([
'Standard_LRS'
])
param type string = 'Standard_LRS'

resource testsa 'Microsoft.Storage/storageAccounts@2021-04-01' = {
  name: name
  location: location
  kind: 'StorageV2'
  sku: {
    name: type
  }
}

output storageId string = testsa.id
