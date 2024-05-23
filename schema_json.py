post_claim_schema={
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "requests": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "body": {
              "type": "object"
            },
            "headers": {
              "type": "array",
              "items": [
                {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string"
                    },
                    "value": {
                      "type": "string"
                    }
                  },
                  "required": [
                    "name",
                    "value"
                  ]
                }
              ]
            },
            "method": {
              "type": "string"
            },
            "onFail": {
              "type": "string"
            },
            "path": {
              "type": "string"
            },
            "query": {
              "type": "string"
            }
          },
          "required": [
            "body",
            "headers",
            "method",
            "onFail",
            "path",
            "query"
          ]
        }
      ]
    }
  },
  "required": [
    "requests"
  ]
}

post_claim_schema_data={
  "requests": [
    {
      "body": {},
      "headers": [
        {
          "name": "api_key",
          "value": "abcd"
        }
      ],
      "method": "delete",
      "onFail": "abort",
      "path": "string",
      "query": "string"
    }
  ]
}
true=True
claiminfo_response={
  "data": {
    "attributes": {
      "archiveState": {
        "code": "string",
        "name": "string"
      },
      "claim": {
        "allValidationLevelsReached": [
          {
            "code": "string",
            "name": "string"
          }
        ],
        "arson": true,
        "assignedByUser": {
          "displayName": "string",
          "id": "string",
          "jsonPath": "string",
          "refid": "string",
          "type": "string",
          "uri": "string"
        },
        "assignedGroup": {
          "displayName": "string",
          "id": "string",
          "jsonPath": "string",
          "refid": "string",
          "type": "string",
          "uri": "string"
        },
        "assignedQueue": {
          "displayName": "string",
          "id": "string",
          "jsonPath": "string",
          "refid": "string",
          "type": "string",
          "uri": "string"
        },
        "assignedUser": {
          "displayName": "string",
          "id": "string",
          "jsonPath": "string",
          "refid": "string",
          "type": "string",
          "uri": "string"
        },
        "assignmentStatus": {
          "code": "string",
          "name": "string"
        },
        "claimNumber": "string",
        "closeDate": "2019-08-24T14:15:22Z",
        "closedOutcome": {
          "code": "string",
          "name": "string"
        },
        "coverageInQuestion": true,
        "description": "string",
        "faultRating": {
          "code": "string",
          "name": "string"
        },
        "filterPropertyRiskUnits": [
          "string"
        ],
        "filterVehicleRiskUnits": [
          "string"
        ],
        "fireDepartmentResponded": true,
        "fireSource": "string",
        "flagged": {
          "code": "string",
          "name": "string"
        },
        "hasWaterBeenTurnedOff": true,
        "howReported": {
          "code": "string",
          "name": "string"
        },
        "howWasFireDiscovered": "string",
        "id": "string",
        "incidentOnly": true,
        "insured": {
          "displayName": "string",
          "id": "string",
          "jsonPath": "string",
          "policySystemId": "string",
          "refid": "string",
          "type": "string",
          "uri": "string"
        },
        "isAnyoneInjured": true,
        "isHomeHabitable": true,
        "isHomeSecure": true,
        "isRoofProtected": true,
        "jurisdiction": {
          "code": "string",
          "name": "string"
        },
        "lobCode": {
          "code": "string",
          "name": "string"
        },
        "lossCause": {
          "code": "string",
          "name": "string"
        },
        "lossDate": "2019-08-24T14:15:22Z",
        "lossLocation": {
          "addressLine1": "string",
          "addressLine2": "string",
          "addressLine3": "string",
          "city": "string",
          "country": "AE",
          "description": "string",
          "displayName": "string",
          "emirate": {
            "code": "string",
            "name": "string"
          },
          "id": "string",
          "policyAddress": true,
          "policyLabel": "string",
          "spatialPoint": {
            "latitude": "string",
            "longitude": "string"
          }
        },
        "lossLocationCode": "strin",
        "lossType": {
          "code": "string",
          "name": "string"
        },
        "mainContact": {
          "displayName": "string",
          "id": "string",
          "jsonPath": "string",
          "policySystemId": "string",
          "refid": "string",
          "type": "string",
          "uri": "string"
        },
        "policyAddresses": [
          {
            "addressLine1": "string",
            "addressLine2": "string",
            "addressLine3": "string",
            "city": "string",
            "country": "AE",
            "description": "string",
            "displayName": "string",
            "emirate": {
              "code": "string",
              "name": "string"
            },
            "id": "string",
            "policyAddress": true,
            "policyLabel": "string",
            "spatialPoint": {
              "latitude": "string",
              "longitude": "string"
            }
          }
        ],
        "policyNumber": "string",
        "reopenDate": "2019-08-24T14:15:22Z",
        "reopenedReason": {
          "code": "string",
          "name": "string"
        },
        "reportedByType": {
          "code": "string",
          "name": "string"
        },
        "reportedDate": "2019-08-24T14:15:22Z",
        "reporter": {
          "displayName": "string",
          "id": "string",
          "jsonPath": "string",
          "policySystemId": "string",
          "refid": "string",
          "type": "string",
          "uri": "string"
        },
        "segment": {
          "code": "string",
          "name": "string"
        },
        "siuStatus": {
          "code": "string",
          "name": "string"
        },
        "smokeDamageOnly": true,
        "state": {
          "code": "string",
          "name": "string"
        },
        "strategy": {
          "code": "string",
          "name": "string"
        },
        "validationLevel": {
          "code": "string",
          "name": "string"
        },
        "waterSource": {
          "code": "string",
          "name": "string"
        },
        "witnesses": [
          {
            "contact": {
              "displayName": "string",
              "id": "string",
              "jsonPath": "string",
              "policySystemId": "string",
              "refid": "string",
              "type": "string",
              "uri": "string"
            },
            "perspective": "string",
            "position": {
              "code": "string",
              "name": "string"
            },
            "statementObtained": {
              "code": "string",
              "name": "string"
            }
          }
        ]
      },
      "claimNumber": "string",
      "id": "string",
      "lossDate": "2019-08-24T14:15:22Z",
      "noticeDate": "2019-08-24T14:15:22Z",
      "policyNumber": "string"
    },
    "checksum": "string",
    "id": "string",
    "links": {
      "property1": {
        "href": "string",
        "methods": [
          "string"
        ]
      },
      "property2": {
        "href": "string",
        "methods": [
          "string"
        ]
      }
    },
    "method": "post",
    "refid": "string",
    "related": {
      "property1": {
        "count": 0,
        "data": [
          {
            "displayName": "string",
            "id": "string",
            "jsonPath": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          }
        ],
        "total": 0
      },
      "property2": {
        "count": 0,
        "data": [
          {
            "displayName": "string",
            "id": "string",
            "jsonPath": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          }
        ],
        "total": 0
      }
    },
    "type": "string",
    "uri": "string"
  }
}
