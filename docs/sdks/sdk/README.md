# SDK

## Overview

### Available Operations

* [send_body](#send_body) - Send a request body of Type Model
* [send_form](#send_form) - Send a form parameter of Type Model

## send_body

Send a request body of Type Model

### Example Usage

```python
from openapi import SDK

s = SDK()

res = s.send_body(query_param={
    "first_property": True,
    "second_property": False,
}, header_param={
    "first_property": False,
    "second_property": False,
}, model={
    "first_property": True,
    "second_property": True,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `query_param`                                                       | [models.Model](../../models/model.md)                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `header_param`                                                      | [models.Model](../../models/model.md)                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `model`                                                             | [models.Model](../../models/model.md)                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ModelOutput](../../models/modeloutput.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |

## send_form

Send a form parameter of Type Model

### Example Usage

```python
from openapi import SDK

s = SDK()

res = s.send_form(query_param={
    "first_property": False,
    "second_property": True,
}, header_param={
    "first_property": False,
    "second_property": True,
}, model={
    "first_property": False,
    "second_property": True,
})

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `query_param`                                                       | [models.Model](../../models/model.md)                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `header_param`                                                      | [models.Model](../../models/model.md)                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `model`                                                             | [models.Model](../../models/model.md)                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ModelOutput](../../models/modeloutput.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.APIError | 4XX, 5XX        | \*/\*           |