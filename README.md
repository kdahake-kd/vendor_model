# Vendor Management API


## Version: v1

### Security
**Basic**  

|basic|*Basic*|
|---|---|

### 1:&nbsp; /purchase_orders/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [PurchaseOrder](#PurchaseOrder) ] |

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [PurchaseOrder](#PurchaseOrder) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [PurchaseOrder](#PurchaseOrder) |

### 2:&nbsp; /purchase_orders/{id}/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this purchase order. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [PurchaseOrder](#PurchaseOrder) |

#### PUT
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this purchase order. | Yes | integer |
| data | body |  | Yes | [PurchaseOrder](#PurchaseOrder) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [PurchaseOrder](#PurchaseOrder) |

#### PATCH
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this purchase order. | Yes | integer |
| data | body |  | Yes | [PurchaseOrder](#PurchaseOrder) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [PurchaseOrder](#PurchaseOrder) |

#### DELETE
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this purchase order. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

###3:&nbsp; /purchase_orders/{id}/acknowledge/

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this purchase order. | Yes | integer |
| data | body |  | Yes | [PurchaseOrder](#PurchaseOrder) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [PurchaseOrder](#PurchaseOrder) |

###4:&nbsp; /vendors/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [ [Vendor](#Vendor) ] |

#### POST
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| data | body |  | Yes | [Vendor](#Vendor) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 |  | [Vendor](#Vendor) |

###5:&nbsp; /vendors/{id}/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this vendor. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Vendor](#Vendor) |

#### PUT
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this vendor. | Yes | integer |
| data | body |  | Yes | [Vendor](#Vendor) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Vendor](#Vendor) |

#### PATCH
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this vendor. | Yes | integer |
| data | body |  | Yes | [Vendor](#Vendor) |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Vendor](#Vendor) |

#### DELETE
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this vendor. | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 |  |

###6:&nbsp; /vendors/{id}/performance/

#### GET
##### Description:



##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | path | A unique integer value identifying this vendor. | Yes | integer |

##### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 |  | [Vendor](#Vendor) |

### Models


#### PurchaseOrder

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| po_number | string |  | Yes |
| order_date | dateTime |  | No |
| delivery_date | dateTime |  | No |
| items | object |  | Yes |
| quantity | integer |  | Yes |
| status | string |  | Yes |
| quality_rating | number |  | No |
| issue_date | dateTime |  | Yes |
| acknowledgment_date | dateTime |  | No |
| vendor | integer |  | Yes |

#### Vendor

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| id | integer |  | No |
| name | string |  | Yes |
| contact_details | string |  | Yes |
| address | string |  | Yes |
| Vendor_code | string |  | Yes |
| on_time_delivery_rate | number |  | No |
| quality_rating_avg | number |  | No |
| average_response_time | number |  | No |
| fulfillment_rate | number |  | No |