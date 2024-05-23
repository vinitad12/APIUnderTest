true=True
request_schema={
  "data": {
    "attributes": {
      "activityPattern": "string",
      "activityType": {
        "code": "string",
        "name": "string"
      },
      "approvalIssue": "string",
      "approvalRationale": "string",
      "assignedByUser": {
        "displayName": "string",
        "id": "string",
        "refid": "string",
        "type": "string",
        "uri": "string"
      },
      "assignedGroup": {
        "displayName": "string",
        "id": "string",
        "refid": "string",
        "type": "string",
        "uri": "string"
      },
      "assignedQueue": {
        "displayName": "string",
        "id": "string",
        "refid": "string",
        "type": "string",
        "uri": "string"
      },
      "assignedUser": {
        "displayName": "string",
        "id": "string",
        "refid": "string",
        "type": "string",
        "uri": "string"
      },
      "assignmentStatus": {
        "code": "string",
        "name": "string"
      },
      "autopilotHandlingDecision": {
        "code": "string",
        "name": "string"
      },
      "autopilotId": "string",
      "autopilotPurpose": {
        "code": "string",
        "name": "string"
      },
      "closeUser": {
        "displayName": "string",
        "id": "string",
        "refid": "string",
        "type": "string",
        "uri": "string"
      },
      "coverageIssues": [
        {
          "coverageSubtype": {
            "code": "string",
            "name": "string"
          },
          "reason": "string",
          "severity": {
            "code": "string",
            "name": "string"
          }
        }
      ],
      "description": "string",
      "dueDate": "2019-08-24T14:15:22Z",
      "endDate": "2019-08-24T14:15:22Z",
      "escalationDate": "2019-08-24T14:15:22Z",
      "externallyOwned": true,
      "importance": {
        "code": "string",
        "name": "string"
      },
      "initialAssignment": {
        "autoAssign": true,
        "claimOwner": true,
        "groupId": "string",
        "queueId": "string",
        "userId": "string"
      },
      "mandatory": true,
      "priority": {
        "code": "string",
        "name": "string"
      },
      "recurring": true,
      "relatedTo": {
        "displayName": "string",
        "id": "string",
        "type": "string",
        "uri": "string"
      },
      "startDate": "2019-08-24T14:15:22Z",
      "status": {
        "code": "string",
        "name": "string"
      },
      "subject": "string"
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
            "refid": "string",
            "type": "string",
            "uri": "string"
          }
        ],
        "total": 0
      }
    },
    "uri": "string"
  },
  "included": {
    "AssessmentContentItem": [
      {
        "attributes": {
          "amountAfterLimit": {
            "amount": "string",
            "currency": "string"
          },
          "contentCategory": {
            "code": "string",
            "name": "string"
          },
          "contentSchedule": {
            "code": "string",
            "name": "string"
          },
          "dateAcquired": "2019-08-24T14:15:22Z",
          "depreciationPercentage": "string",
          "description": "string",
          "incidentOrder": 0,
          "itemComment": "string",
          "numberOfItems": 0,
          "purchaseCost": {
            "amount": "string",
            "currency": "string"
          },
          "replacementValue": {
            "amount": "string",
            "currency": "string"
          }
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "AssessmentSummary": [
      {
        "attributes": {
          "category": "string",
          "exposure": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "normalizedScore": "string",
          "rawAssessmentReferenceId": "string",
          "recommendedActionCode": "string",
          "recommendedActionDescription": "string",
          "score": "string",
          "scoreDate": "2019-08-24T14:15:22Z",
          "scorePercentile": "string",
          "tapId": "string",
          "tapSubtypeId": "string"
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "BaggageIncident": [
      {
        "attributes": {
          "baggageMissingFrom": "2019-08-24T14:15:22Z",
          "baggageRecoveredOn": "2019-08-24T14:15:22Z",
          "baggageType": {
            "code": "string",
            "name": "string"
          },
          "carrierCompensated": true,
          "carrierCompensatedAmount": {
            "amount": "string",
            "currency": "string"
          },
          "delayOnly": true,
          "description": "string",
          "incidentOwner": {
            "displayName": "string",
            "id": "string",
            "policySystemId": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "relatedTripRiskUnit": {
            "displayName": "string",
            "id": "string",
            "policySystemId": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "severity": {
            "code": "string",
            "name": "string"
          }
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "ClaimContact": [
      {
        "attributes": {
          "addressBookUID": "string",
          "companyName": "string",
          "companyNameKanji": "string",
          "contactSubtype": "AutoRepairShop",
          "editableRoles": [
            {
              "active": true,
              "comments": "string",
              "relatedTo": {
                "displayName": "string",
                "id": "string",
                "type": "string",
                "uri": "string"
              },
              "role": {
                "code": "string",
                "name": "string"
              }
            }
          ],
          "emailAddress1": "string",
          "emailAddress2": "string",
          "primaryAddress": {
            "addressLine1": "string",
            "addressLine2": "string",
            "addressLine3": "string",
            "addressType": {
              "code": "string",
              "name": "string"
            },
            "city": "string",
            "country": "AE",
            "description": "string",
            "emirate": {
              "code": "string",
              "name": "string"
            },
            "spatialPoint": {
              "latitude": "string",
              "longitude": "string"
            },
            "validUntil": "2019-08-24T14:15:22Z"
          },
          "primaryLanguage": {
            "code": "string",
            "name": "string"
          },
          "primaryLocale": {
            "code": "string",
            "name": "string"
          },
          "syncAddressBookUID": "string",
          "taxId": "string",
          "workPhone": {
            "countryCode": {
              "code": "string",
              "name": "string"
            },
            "extension": "string",
            "number": "string"
          }
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "DwellingIncident": [
      {
        "attributes": {
          "automationPath": {
            "code": "string",
            "name": "string"
          },
          "damagedAreaSize": 0,
          "description": "string",
          "dwellingRoomDamages": [
            {
              "id": "string",
              "numberOfRooms": 0,
              "roomType": {
                "code": "string",
                "name": "string"
              }
            }
          ],
          "fireProtectionAvailable": true,
          "incidentOwner": {
            "displayName": "string",
            "id": "string",
            "policySystemId": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "location": {
            "address": {
              "addressLine1": "string",
              "addressLine2": "string",
              "addressLine3": "string",
              "city": "string",
              "country": "AE",
              "description": "string",
              "emirate": {
                "code": "string",
                "name": "string"
              },
              "id": "string",
              "policyLabel": "string",
              "spatialPoint": {
                "latitude": "string",
                "longitude": "string"
              }
            },
            "buildings": [
              {
                "buildingNumber": "string",
                "id": "string",
                "notes": "string"
              }
            ],
            "id": "string",
            "locationNumber": "string",
            "notes": "string",
            "policySystemId": "string",
            "primaryLocation": true
          },
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "materialsDamaged": "string",
          "numberOfPeopleOnPolicy": 0,
          "occupancyType": {
            "code": "string",
            "name": "string"
          },
          "propertySize": 0,
          "severity": {
            "code": "string",
            "name": "string"
          },
          "yearBuilt": "2019-08-24T14:15:22Z",
          "yearsInHome": 0
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "Exposure": [
      {
        "attributes": {
          "assignedByUser": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "assignedGroup": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "assignedQueue": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "assignedUser": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "assignmentStatus": {
            "code": "string",
            "name": "string"
          },
          "autopilotStatus": {
            "code": "string",
            "name": "string"
          },
          "baggageIncident": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "claimOrder": 0,
          "claimant": {
            "displayName": "string",
            "id": "string",
            "policySystemId": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "claimantType": {
            "code": "string",
            "name": "string"
          },
          "closedOutcome": {
            "code": "string",
            "name": "string"
          },
          "contactPermitted": true,
          "coverage": {
            "displayName": "string",
            "id": "string",
            "policySystemId": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "coverageSubtype": {
            "code": "string",
            "name": "string"
          },
          "createdVia": {
            "code": "string",
            "name": "string"
          },
          "deductible": {
            "amount": {
              "amount": "string",
              "currency": "string"
            },
            "amountApplied": {
              "amount": "string",
              "currency": "string"
            },
            "amountRemaining": {
              "amount": "string",
              "currency": "string"
            },
            "waived": true
          },
          "dwellingIncident": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "externalStatus": {
            "code": "string",
            "name": "string"
          },
          "fixedPropertyIncident": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "generalIncident": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "injuryIncident": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "jurisdiction": {
            "code": "string",
            "name": "string"
          },
          "livingExpensesIncident": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "lossCategory": {
            "code": "string",
            "name": "string"
          },
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "otherCoverage": true,
          "otherStructureIncident": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "primaryCoverage": {
            "code": "string",
            "name": "string"
          },
          "progress": {
            "code": "string",
            "name": "string"
          },
          "propertyContentsIncident": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "reopenedReason": {
            "code": "string",
            "name": "string"
          },
          "securityLevel": {
            "code": "string",
            "name": "string"
          },
          "segment": {
            "code": "string",
            "name": "string"
          },
          "state": {
            "code": "string",
            "name": "string"
          },
          "strategy": {
            "code": "string",
            "name": "string"
          },
          "tier": {
            "code": "string",
            "name": "string"
          },
          "tripIncident": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "type": {
            "code": "string",
            "name": "string"
          },
          "validationLevel": {
            "code": "string",
            "name": "string"
          },
          "vehicleIncident": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          }
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "FixedPropertyIncident": [
      {
        "attributes": {
          "automationPath": {
            "code": "string",
            "name": "string"
          },
          "description": "string",
          "id": "string",
          "incidentOwner": {
            "displayName": "string",
            "id": "string",
            "policySystemId": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "location": {
            "address": {
              "addressLine1": "string",
              "addressLine2": "string",
              "addressLine3": "string",
              "city": "string",
              "country": "AE",
              "description": "string",
              "emirate": {
                "code": "string",
                "name": "string"
              },
              "id": "string",
              "policyLabel": "string",
              "spatialPoint": {
                "latitude": "string",
                "longitude": "string"
              }
            },
            "buildings": [
              {
                "buildingNumber": "string",
                "id": "string",
                "notes": "string"
              }
            ],
            "id": "string",
            "locationNumber": "string",
            "notes": "string",
            "policySystemId": "string",
            "primaryLocation": true
          },
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "occupancyType": {
            "code": "string",
            "name": "string"
          },
          "severity": {
            "code": "string",
            "name": "string"
          }
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "GeneralIncident": [
      {
        "attributes": {
          "description": "string",
          "incidentOwner": {
            "displayName": "string",
            "id": "string",
            "policySystemId": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "severity": {
            "code": "string",
            "name": "string"
          }
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "InjuryIncident": [
      {
        "attributes": {
          "ambulanceUsed": true,
          "automationPath": {
            "code": "string",
            "name": "string"
          },
          "bodyParts": [
            {
              "detailedBodyPart": {
                "code": "string",
                "name": "string"
              },
              "detailedBodyPartDesc": {
                "code": "string",
                "name": "string"
              },
              "id": "string",
              "impairmentPercentage": 0,
              "ordering": 0,
              "primaryBodyPart": {
                "code": "string",
                "name": "string"
              },
              "sideOfBody": {
                "code": "string",
                "name": "string"
              }
            }
          ],
          "dateOfDeath": "2019-08-24T14:15:22Z",
          "description": "string",
          "detailedInjuryType": {
            "code": "string",
            "name": "string"
          },
          "disabledDueToAccident": {
            "code": "string",
            "name": "string"
          },
          "generalInjuryType": {
            "code": "string",
            "name": "string"
          },
          "id": "string",
          "injuredPerson": {
            "displayName": "string",
            "id": "string",
            "policySystemId": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "lostWages": true,
          "primaryDoctor": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "severity": {
            "code": "string",
            "name": "string"
          },
          "treatmentType": {
            "code": "string",
            "name": "string"
          }
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "LivingExpensesIncident": [
      {
        "attributes": {
          "automationPath": {
            "code": "string",
            "name": "string"
          },
          "description": "string",
          "id": "string",
          "incidentOwner": {
            "displayName": "string",
            "id": "string",
            "policySystemId": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "startDate": "2019-08-24T14:15:22Z"
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "Matter": [
      {
        "attributes": {
          "adDamnumAmount": {
            "amount": "string",
            "currency": "string"
          },
          "adDamnumSpecified": true,
          "arbitrationDate": "2019-08-24T14:15:22Z",
          "arbitrationRoom": "string",
          "assignedByUser": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "assignedGroup": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "assignedQueue": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "assignedUser": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "assignmentStatus": {
            "code": "string",
            "name": "string"
          },
          "caseNumber": "string",
          "courtDistrict": {
            "code": "string",
            "name": "string"
          },
          "courtType": {
            "code": "string",
            "name": "string"
          },
          "defenseAppointmentDate": "2019-08-24T14:15:22Z",
          "docketNumber": "string",
          "fileDate": "2019-08-24T14:15:22Z",
          "finalLegalCost": {
            "amount": "string",
            "currency": "string"
          },
          "finalSettlementCost": {
            "amount": "string",
            "currency": "string"
          },
          "finalSettlementDate": "2019-08-24T14:15:22Z",
          "hearingDate": "2019-08-24T14:15:22Z",
          "hearingRoom": "string",
          "id": "string",
          "legalSpecialty": {
            "code": "string",
            "name": "string"
          },
          "matterType": {
            "code": "string",
            "name": "string"
          },
          "mediationDate": "2019-08-24T14:15:22Z",
          "mediationRoom": "string",
          "methodServed": {
            "code": "string",
            "name": "string"
          },
          "name": "string",
          "primaryCause": {
            "code": "string",
            "name": "string"
          },
          "punitiveAmount": {
            "amount": "string",
            "currency": "string"
          },
          "punitiveDamages": true,
          "reopenedReason": {
            "code": "string",
            "name": "string"
          },
          "resolution": {
            "code": "string",
            "name": "string"
          },
          "responseDue": "2019-08-24",
          "responseFiled": "2019-08-24",
          "room": "string",
          "sentToDefenseDate": "2019-08-24T14:15:22Z",
          "serviceDate": "2019-08-24",
          "subrogationRelated": true,
          "trialDate": "2019-08-24T14:15:22Z",
          "validationLevel": {
            "code": "string",
            "name": "string"
          }
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "Note": [
      {
        "attributes": {
          "author": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "body": "string",
          "confidential": true,
          "relatedTo": {
            "displayName": "string",
            "id": "string",
            "type": "string",
            "uri": "string"
          },
          "securityType": {
            "code": "string",
            "name": "string"
          },
          "subject": "string",
          "topic": {
            "code": "string",
            "name": "string"
          }
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "OtherStructureIncident": [
      {
        "attributes": {
          "description": "string",
          "fencesDamaged": true,
          "incidentOwner": {
            "displayName": "string",
            "id": "string",
            "policySystemId": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "severity": {
            "code": "string",
            "name": "string"
          }
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "PropertyContentsIncident": [
      {
        "attributes": {
          "description": "string",
          "incidentOwner": {
            "displayName": "string",
            "id": "string",
            "policySystemId": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "location": {
            "address": {
              "addressLine1": "string",
              "addressLine2": "string",
              "addressLine3": "string",
              "city": "string",
              "country": "AE",
              "description": "string",
              "emirate": {
                "code": "string",
                "name": "string"
              },
              "id": "string",
              "policyLabel": "string",
              "spatialPoint": {
                "latitude": "string",
                "longitude": "string"
              }
            },
            "buildings": [
              {
                "buildingNumber": "string",
                "id": "string",
                "notes": "string"
              }
            ],
            "id": "string",
            "locationNumber": "string",
            "notes": "string",
            "policySystemId": "string",
            "primaryLocation": true
          },
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "severity": {
            "code": "string",
            "name": "string"
          }
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "PropertyContentsScheduledItem": [
      {
        "attributes": {
          "propertyItem": {
            "displayName": "string",
            "id": "string",
            "policySystemId": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          }
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "ServiceRequest": [
      {
        "attributes": {
          "assignedGroup": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "assignedUser": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "claim": {
            "claimNumber": "string",
            "displayName": "string",
            "id": "string",
            "type": "string",
            "uri": "string"
          },
          "exposure": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "incident": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "instruction": {
            "customer": {
              "displayName": "string",
              "id": "string",
              "policySystemId": "string",
              "refid": "string",
              "type": "string",
              "uri": "string"
            },
            "instructionText": "string",
            "serviceAddress": {
              "addressLine1": "string",
              "addressLine2": "string",
              "addressLine3": "string",
              "city": "string",
              "country": "AE",
              "description": "string",
              "emirate": {
                "code": "string",
                "name": "string"
              },
              "id": "string",
              "policyLabel": "string",
              "spatialPoint": {
                "latitude": "string",
                "longitude": "string"
              }
            },
            "services": [
              {
                "code": "string",
                "parent": {
                  "code": "string",
                  "displayName": "string"
                }
              }
            ]
          },
          "kind": {
            "code": "string",
            "name": "string"
          },
          "latestQuote": {
            "approvedBy": {
              "displayName": "string",
              "id": "string",
              "refid": "string",
              "type": "string",
              "uri": "string"
            },
            "description": "string",
            "expectedDaysToPerformService": 0,
            "lineItems": [
              {
                "amount": {
                  "amount": "string",
                  "currency": "string"
                },
                "category": {
                  "code": "string",
                  "name": "string"
                },
                "description": "string"
              }
            ],
            "operationContext": {},
            "paymentDate": "2019-08-24",
            "paymentDateTime": "2019-08-24T14:15:22Z",
            "referenceNumber": "string",
            "source": {
              "code": "string",
              "name": "string"
            },
            "status": {
              "code": "string",
              "name": "string"
            },
            "subtype": {
              "code": "string",
              "name": "string"
            },
            "total": {
              "amount": "string",
              "currency": "string"
            }
          },
          "nextStep": {
            "defaultOperation": "string",
            "name": "string"
          },
          "progress": {
            "code": "string",
            "name": "string"
          },
          "quoteStatus": {
            "code": "string",
            "name": "string"
          },
          "referenceNumber": "string",
          "requestedQuoteCompletionDate": "2019-08-24",
          "requestedQuoteCompletionDateTime": "2019-08-24T14:15:22Z",
          "requestedServiceCompletionDate": "2019-08-24",
          "requestedServiceCompletionDateTime": "2019-08-24T14:15:22Z",
          "specialist": {
            "displayName": "string",
            "id": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "specialistCommMethod": {
            "code": "string",
            "name": "string"
          },
          "tier": {
            "code": "string",
            "name": "string"
          }
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "TripAccommodation": [
      {
        "attributes": {
          "address": {
            "addressLine1": "string",
            "addressLine2": "string",
            "addressLine3": "string",
            "city": "string",
            "country": "AE",
            "description": "string",
            "emirate": {
              "code": "string",
              "name": "string"
            },
            "id": "string",
            "policyLabel": "string",
            "spatialPoint": {
              "latitude": "string",
              "longitude": "string"
            }
          },
          "agentFees": {
            "amount": "string",
            "currency": "string"
          },
          "assessment": {
            "code": "string",
            "name": "string"
          },
          "cancelOnly": true,
          "cancellationFees": {
            "amount": "string",
            "currency": "string"
          },
          "checkinDateTime": "2019-08-24T14:15:22Z",
          "checkoutDateTime": "2019-08-24T14:15:22Z",
          "otherFees": {
            "amount": "string",
            "currency": "string"
          },
          "paidAmount": {
            "amount": "string",
            "currency": "string"
          },
          "propertyName": "string",
          "reasonForCancellation": "string",
          "reasonForDenial": "string"
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "TripIncident": [
      {
        "attributes": {
          "description": "string",
          "incidentOwner": {
            "displayName": "string",
            "id": "string",
            "policySystemId": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "severity": {
            "code": "string",
            "name": "string"
          },
          "tripRiskUnit": {
            "displayName": "string",
            "id": "string",
            "policySystemId": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          }
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "TripSegment": [
      {
        "attributes": {
          "agentFees": {
            "amount": "string",
            "currency": "string"
          },
          "arrivalDateTime": "2019-08-24T14:15:22Z",
          "assessment": {
            "code": "string",
            "name": "string"
          },
          "cancelOnly": true,
          "cancellationFees": {
            "amount": "string",
            "currency": "string"
          },
          "carrierName": "string",
          "carrierNumber": "string",
          "departureDateTime": "2019-08-24T14:15:22Z",
          "otherFees": {
            "amount": "string",
            "currency": "string"
          },
          "paidAmount": {
            "amount": "string",
            "currency": "string"
          },
          "portOfDisembarkation": "string",
          "portOfEmbarkation": "string",
          "reasonForCancellation": "string",
          "reasonForDenial": "string",
          "transportType": {
            "code": "string",
            "name": "string"
          }
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "UnverifiedPropertyItem": [
      {
        "attributes": {
          "appraisedValue": {
            "amount": "string",
            "currency": "string"
          },
          "description": "string"
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "VehicleIncident": [
      {
        "attributes": {
          "airbagsDeployed": true,
          "automationPath": {
            "code": "string",
            "name": "string"
          },
          "childSafetySeatStatus": {
            "code": "string",
            "name": "string"
          },
          "collision": true,
          "collisionPoint": {
            "code": "string",
            "name": "string"
          },
          "damageDescription": "string",
          "driver": {
            "displayName": "string",
            "id": "string",
            "policySystemId": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "equipmentFailure": true,
          "id": "string",
          "incidentOwner": {
            "displayName": "string",
            "id": "string",
            "policySystemId": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "numOccupants": 0,
          "passengers": [
            {
              "displayName": "string",
              "id": "string",
              "policySystemId": "string",
              "refid": "string",
              "type": "string",
              "uri": "string"
            }
          ],
          "propertyDamageDescription": "string",
          "propertyValue": {
            "amount": "string",
            "currency": "string"
          },
          "safeToDrive": true,
          "severity": {
            "code": "string",
            "name": "string"
          },
          "theft": true,
          "totalLoss": true,
          "valuationRequired": {
            "code": "string",
            "name": "string"
          },
          "valuationSource": {
            "code": "string",
            "name": "string"
          },
          "vehicle": {
            "color": "string",
            "id": "string",
            "licensePlate": "string",
            "make": "string",
            "manufacturer": {
              "code": "string",
              "name": "string"
            },
            "model": "string",
            "policySystemId": "string",
            "state": {
              "code": "string",
              "name": "string"
            },
            "style": {
              "code": "string",
              "name": "string"
            },
            "vin": "string",
            "year": 0
          },
          "vehicleDirection": {
            "code": "string",
            "name": "string"
          },
          "vehicleParked": true,
          "vehicleType": {
            "code": "string",
            "name": "string"
          },
          "vehicleUseReason": {
            "code": "string",
            "name": "string"
          }
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
                "refid": "string",
                "type": "string",
                "uri": "string"
              }
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ]
  }
}

request_payload_sample={
  "data": {
    "attributes": {
      "activityPattern": "string",
      "activityType": {
        "code": "string",
        "name": "string"
      },
      "approvalIssue": "string",
      "approvalRationale": "string",
      "assignedByUser": "quis",
      "assignedGroup": "quis",
      "assignedQueue": "quis",
      "assignedUser": "quis",
      "assignmentStatus": {
        "code": "string",
        "name": "string"
      },
      "autopilotHandlingDecision": {
        "code": "string",
        "name": "string"
      },
      "autopilotId": "string",
      "autopilotPurpose": {
        "code": "string",
        "name": "string"
      },
      "closeUser": "quis",
      "coverageIssues": [
        {
          "coverageSubtype": {
            "code": "string",
            "name": "string"
          },
          "reason": "string",
          "severity": {
            "code": "string",
            "name": "string"
          }
        }
      ],
      "description": "string",
      "dueDate": "2019-08-24T14:15:22Z",
      "endDate": "2019-08-24T14:15:22Z",
      "escalationDate": "2019-08-24T14:15:22Z",
      "externallyOwned": true,
      "importance": {
        "code": "string",
        "name": "string"
      },
      "initialAssignment": {
        "autoAssign": true,
        "claimOwner": true,
        "groupId": "string",
        "queueId": "string",
        "userId": "string"
      },
      "mandatory": true,
      "priority": {
        "code": "string",
        "name": "string"
      },
      "recurring": true,
      "relatedTo": "quis",
      "startDate": "2019-08-24T14:15:22Z",
      "status": {
        "code": "string",
        "name": "string"
      },
      "subject": "string"
    },
    "checksum": "string",
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
          "quis"
        ],
        "total": 0
      },
      "property2": {
        "count": 0,
        "data": [
          "quis"
        ],
        "total": 0
      }
    },
    "uri": "string"
  },
  "included": {
    "AssessmentContentItem": [
      {
        "attributes": {
          "amountAfterLimit": {
            "amount": "string",
            "currency": "string"
          },
          "contentCategory": {
            "code": "string",
            "name": "string"
          },
          "contentSchedule": {
            "code": "string",
            "name": "string"
          },
          "dateAcquired": "2019-08-24T14:15:22Z",
          "depreciationPercentage": "string",
          "description": "string",
          "incidentOrder": 0,
          "itemComment": "string",
          "numberOfItems": 0,
          "purchaseCost": {
            "amount": "string",
            "currency": "string"
          },
          "replacementValue": {
            "amount": "string",
            "currency": "string"
          }
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "AssessmentSummary": [
      {
        "attributes": {
          "category": "string",
          "exposure": "quis",
          "normalizedScore": "string",
          "rawAssessmentReferenceId": "string",
          "recommendedActionCode": "string",
          "recommendedActionDescription": "string",
          "score": "string",
          "scoreDate": "2019-08-24T14:15:22Z",
          "scorePercentile": "string",
          "tapId": "string",
          "tapSubtypeId": "string"
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "BaggageIncident": [
      {
        "attributes": {
          "baggageMissingFrom": "2019-08-24T14:15:22Z",
          "baggageRecoveredOn": "2019-08-24T14:15:22Z",
          "baggageType": {
            "code": "string",
            "name": "string"
          },
          "carrierCompensated": true,
          "carrierCompensatedAmount": {
            "amount": "string",
            "currency": "string"
          },
          "delayOnly": true,
          "description": "string",
          "incidentOwner": "quis",
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "relatedTripRiskUnit": "quis",
          "severity": {
            "code": "string",
            "name": "string"
          }
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "ClaimContact": [
      {
        "attributes": {
          "addressBookUID": "string",
          "companyName": "string",
          "companyNameKanji": "string",
          "contactSubtype": "AutoRepairShop",
          "editableRoles": [
            {
              "active": true,
              "comments": "string",
              "relatedTo": "quis",
              "role": {
                "code": "string",
                "name": "string"
              }
            }
          ],
          "emailAddress1": "string",
          "emailAddress2": "string",
          "primaryAddress": {
            "addressLine1": "string",
            "addressLine2": "string",
            "addressLine3": "string",
            "addressType": {
              "code": "string",
              "name": "string"
            },
            "city": "string",
            "country": "AE",
            "description": "string",
            "emirate": {
              "code": "string",
              "name": "string"
            },
            "spatialPoint": {
              "latitude": "string",
              "longitude": "string"
            },
            "validUntil": "2019-08-24T14:15:22Z"
          },
          "primaryLanguage": {
            "code": "string",
            "name": "string"
          },
          "primaryLocale": {
            "code": "string",
            "name": "string"
          },
          "syncAddressBookUID": "string",
          "taxId": "string",
          "workPhone": {
            "countryCode": {
              "code": "string",
              "name": "string"
            },
            "extension": "string",
            "number": "string"
          }
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "DwellingIncident": [
      {
        "attributes": {
          "automationPath": {
            "code": "string",
            "name": "string"
          },
          "damagedAreaSize": 0,
          "description": "string",
          "dwellingRoomDamages": [
            {
              "numberOfRooms": 0,
              "roomType": {
                "code": "string",
                "name": "string"
              }
            }
          ],
          "fireProtectionAvailable": true,
          "incidentOwner": "quis",
          "location": {
            "address": {
              "addressLine1": "string",
              "addressLine2": "string",
              "addressLine3": "string",
              "city": "string",
              "country": "AE",
              "description": "string",
              "emirate": {
                "code": "string",
                "name": "string"
              },
              "policyLabel": "string",
              "spatialPoint": {
                "latitude": "string",
                "longitude": "string"
              }
            },
            "buildings": [
              {
                "buildingNumber": "string",
                "notes": "string"
              }
            ],
            "locationNumber": "string",
            "notes": "string",
            "policySystemId": "string",
            "primaryLocation": true
          },
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "materialsDamaged": "string",
          "numberOfPeopleOnPolicy": 0,
          "occupancyType": {
            "code": "string",
            "name": "string"
          },
          "propertySize": 0,
          "severity": {
            "code": "string",
            "name": "string"
          },
          "yearBuilt": "2019-08-24T14:15:22Z",
          "yearsInHome": 0
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "Exposure": [
      {
        "attributes": {
          "assignedByUser": "quis",
          "assignedGroup": "quis",
          "assignedQueue": "quis",
          "assignedUser": "quis",
          "assignmentStatus": {
            "code": "string",
            "name": "string"
          },
          "autopilotStatus": {
            "code": "string",
            "name": "string"
          },
          "baggageIncident": "quis",
          "claimOrder": 0,
          "claimant": "quis",
          "claimantType": {
            "code": "string",
            "name": "string"
          },
          "closedOutcome": {
            "code": "string",
            "name": "string"
          },
          "contactPermitted": true,
          "coverage": "quis",
          "coverageSubtype": {
            "code": "string",
            "name": "string"
          },
          "createdVia": {
            "code": "string",
            "name": "string"
          },
          "deductible": {
            "amount": {
              "amount": "string",
              "currency": "string"
            },
            "amountApplied": {
              "amount": "string",
              "currency": "string"
            },
            "amountRemaining": {
              "amount": "string",
              "currency": "string"
            },
            "waived": true
          },
          "dwellingIncident": "quis",
          "externalStatus": {
            "code": "string",
            "name": "string"
          },
          "fixedPropertyIncident": "quis",
          "generalIncident": "quis",
          "injuryIncident": "quis",
          "jurisdiction": {
            "code": "string",
            "name": "string"
          },
          "livingExpensesIncident": "quis",
          "lossCategory": {
            "code": "string",
            "name": "string"
          },
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "otherCoverage": true,
          "otherStructureIncident": "quis",
          "primaryCoverage": {
            "code": "string",
            "name": "string"
          },
          "progress": {
            "code": "string",
            "name": "string"
          },
          "propertyContentsIncident": "quis",
          "reopenedReason": {
            "code": "string",
            "name": "string"
          },
          "securityLevel": {
            "code": "string",
            "name": "string"
          },
          "segment": {
            "code": "string",
            "name": "string"
          },
          "state": {
            "code": "string",
            "name": "string"
          },
          "strategy": {
            "code": "string",
            "name": "string"
          },
          "tier": {
            "code": "string",
            "name": "string"
          },
          "tripIncident": "quis",
          "type": {
            "code": "string",
            "name": "string"
          },
          "validationLevel": {
            "code": "string",
            "name": "string"
          },
          "vehicleIncident": "quis"
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "FixedPropertyIncident": [
      {
        "attributes": {
          "automationPath": {
            "code": "string",
            "name": "string"
          },
          "description": "string",
          "incidentOwner": "quis",
          "location": {
            "address": {
              "addressLine1": "string",
              "addressLine2": "string",
              "addressLine3": "string",
              "city": "string",
              "country": "AE",
              "description": "string",
              "emirate": {
                "code": "string",
                "name": "string"
              },
              "policyLabel": "string",
              "spatialPoint": {
                "latitude": "string",
                "longitude": "string"
              }
            },
            "buildings": [
              {
                "buildingNumber": "string",
                "notes": "string"
              }
            ],
            "locationNumber": "string",
            "notes": "string",
            "policySystemId": "string",
            "primaryLocation": true
          },
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "occupancyType": {
            "code": "string",
            "name": "string"
          },
          "severity": {
            "code": "string",
            "name": "string"
          }
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "GeneralIncident": [
      {
        "attributes": {
          "description": "string",
          "incidentOwner": "quis",
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "severity": {
            "code": "string",
            "name": "string"
          }
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "InjuryIncident": [
      {
        "attributes": {
          "ambulanceUsed": true,
          "automationPath": {
            "code": "string",
            "name": "string"
          },
          "bodyParts": [
            {
              "detailedBodyPart": {
                "code": "string",
                "name": "string"
              },
              "detailedBodyPartDesc": {
                "code": "string",
                "name": "string"
              },
              "impairmentPercentage": 0,
              "ordering": 0,
              "primaryBodyPart": {
                "code": "string",
                "name": "string"
              },
              "sideOfBody": {
                "code": "string",
                "name": "string"
              }
            }
          ],
          "dateOfDeath": "2019-08-24T14:15:22Z",
          "description": "string",
          "detailedInjuryType": {
            "code": "string",
            "name": "string"
          },
          "disabledDueToAccident": {
            "code": "string",
            "name": "string"
          },
          "generalInjuryType": {
            "code": "string",
            "name": "string"
          },
          "injuredPerson": "quis",
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "lostWages": true,
          "primaryDoctor": "quis",
          "severity": {
            "code": "string",
            "name": "string"
          },
          "treatmentType": {
            "code": "string",
            "name": "string"
          }
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "LivingExpensesIncident": [
      {
        "attributes": {
          "automationPath": {
            "code": "string",
            "name": "string"
          },
          "description": "string",
          "incidentOwner": "quis",
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "startDate": "2019-08-24T14:15:22Z"
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "Matter": [
      {
        "attributes": {
          "adDamnumAmount": {
            "amount": "string",
            "currency": "string"
          },
          "adDamnumSpecified": true,
          "arbitrationDate": "2019-08-24T14:15:22Z",
          "arbitrationRoom": "string",
          "assignedByUser": "quis",
          "assignedGroup": "quis",
          "assignedQueue": "quis",
          "assignedUser": "quis",
          "assignmentStatus": {
            "code": "string",
            "name": "string"
          },
          "caseNumber": "string",
          "courtDistrict": {
            "code": "string",
            "name": "string"
          },
          "courtType": {
            "code": "string",
            "name": "string"
          },
          "defenseAppointmentDate": "2019-08-24T14:15:22Z",
          "docketNumber": "string",
          "fileDate": "2019-08-24T14:15:22Z",
          "finalLegalCost": {
            "amount": "string",
            "currency": "string"
          },
          "finalSettlementCost": {
            "amount": "string",
            "currency": "string"
          },
          "finalSettlementDate": "2019-08-24T14:15:22Z",
          "hearingDate": "2019-08-24T14:15:22Z",
          "hearingRoom": "string",
          "legalSpecialty": {
            "code": "string",
            "name": "string"
          },
          "matterType": {
            "code": "string",
            "name": "string"
          },
          "mediationDate": "2019-08-24T14:15:22Z",
          "mediationRoom": "string",
          "methodServed": {
            "code": "string",
            "name": "string"
          },
          "name": "string",
          "primaryCause": {
            "code": "string",
            "name": "string"
          },
          "punitiveAmount": {
            "amount": "string",
            "currency": "string"
          },
          "punitiveDamages": true,
          "reopenedReason": {
            "code": "string",
            "name": "string"
          },
          "resolution": {
            "code": "string",
            "name": "string"
          },
          "responseDue": "2019-08-24",
          "responseFiled": "2019-08-24",
          "room": "string",
          "sentToDefenseDate": "2019-08-24T14:15:22Z",
          "serviceDate": "2019-08-24",
          "subrogationRelated": true,
          "trialDate": "2019-08-24T14:15:22Z",
          "validationLevel": {
            "code": "string",
            "name": "string"
          }
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "Note": [
      {
        "attributes": {
          "author": "quis",
          "body": "string",
          "confidential": true,
          "relatedTo": "quis",
          "securityType": {
            "code": "string",
            "name": "string"
          },
          "subject": "string",
          "topic": {
            "code": "string",
            "name": "string"
          }
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "OtherStructureIncident": [
      {
        "attributes": {
          "description": "string",
          "fencesDamaged": true,
          "incidentOwner": "quis",
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "severity": {
            "code": "string",
            "name": "string"
          }
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "PropertyContentsIncident": [
      {
        "attributes": {
          "description": "string",
          "incidentOwner": "quis",
          "location": {
            "address": {
              "addressLine1": "string",
              "addressLine2": "string",
              "addressLine3": "string",
              "city": "string",
              "country": "AE",
              "description": "string",
              "emirate": {
                "code": "string",
                "name": "string"
              },
              "policyLabel": "string",
              "spatialPoint": {
                "latitude": "string",
                "longitude": "string"
              }
            },
            "buildings": [
              {
                "buildingNumber": "string",
                "notes": "string"
              }
            ],
            "locationNumber": "string",
            "notes": "string",
            "policySystemId": "string",
            "primaryLocation": true
          },
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "severity": {
            "code": "string",
            "name": "string"
          }
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "PropertyContentsScheduledItem": [
      {
        "attributes": {
          "propertyItem": "quis"
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "ServiceRequest": [
      {
        "attributes": {
          "assignedGroup": "quis",
          "assignedUser": "quis",
          "claim": "quis",
          "exposure": "quis",
          "incident": "quis",
          "instruction": {
            "customer": "quis",
            "instructionText": "string",
            "serviceAddress": {
              "addressLine1": "string",
              "addressLine2": "string",
              "addressLine3": "string",
              "city": "string",
              "country": "AE",
              "description": "string",
              "emirate": {
                "code": "string",
                "name": "string"
              },
              "policyLabel": "string",
              "spatialPoint": {
                "latitude": "string",
                "longitude": "string"
              }
            },
            "services": [
              {
                "code": "string",
                "parent": {
                  "code": "string",
                  "displayName": "string"
                }
              }
            ]
          },
          "kind": {
            "code": "string",
            "name": "string"
          },
          "latestQuote": {
            "approvedBy": "quis",
            "description": "string",
            "expectedDaysToPerformService": 0,
            "lineItems": [
              {
                "amount": {
                  "amount": "string",
                  "currency": "string"
                },
                "category": {
                  "code": "string",
                  "name": "string"
                },
                "description": "string"
              }
            ],
            "paymentDate": "2019-08-24",
            "paymentDateTime": "2019-08-24T14:15:22Z",
            "referenceNumber": "string",
            "source": {
              "code": "string",
              "name": "string"
            },
            "status": {
              "code": "string",
              "name": "string"
            },
            "subtype": {
              "code": "string",
              "name": "string"
            },
            "total": {
              "amount": "string",
              "currency": "string"
            }
          },
          "nextStep": {
            "defaultOperation": "string",
            "name": "string"
          },
          "progress": {
            "code": "string",
            "name": "string"
          },
          "quoteStatus": {
            "code": "string",
            "name": "string"
          },
          "referenceNumber": "string",
          "requestedQuoteCompletionDate": "2019-08-24",
          "requestedQuoteCompletionDateTime": "2019-08-24T14:15:22Z",
          "requestedServiceCompletionDate": "2019-08-24",
          "requestedServiceCompletionDateTime": "2019-08-24T14:15:22Z",
          "specialist": "quis",
          "specialistCommMethod": {
            "code": "string",
            "name": "string"
          },
          "tier": {
            "code": "string",
            "name": "string"
          }
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "TripAccommodation": [
      {
        "attributes": {
          "address": {
            "addressLine1": "string",
            "addressLine2": "string",
            "addressLine3": "string",
            "city": "string",
            "country": "AE",
            "description": "string",
            "emirate": {
              "code": "string",
              "name": "string"
            },
            "policyLabel": "string",
            "spatialPoint": {
              "latitude": "string",
              "longitude": "string"
            }
          },
          "agentFees": {
            "amount": "string",
            "currency": "string"
          },
          "assessment": {
            "code": "string",
            "name": "string"
          },
          "cancelOnly": true,
          "cancellationFees": {
            "amount": "string",
            "currency": "string"
          },
          "checkinDateTime": "2019-08-24T14:15:22Z",
          "checkoutDateTime": "2019-08-24T14:15:22Z",
          "otherFees": {
            "amount": "string",
            "currency": "string"
          },
          "paidAmount": {
            "amount": "string",
            "currency": "string"
          },
          "propertyName": "string",
          "reasonForCancellation": "string",
          "reasonForDenial": "string"
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "TripIncident": [
      {
        "attributes": {
          "description": "string",
          "incidentOwner": "quis",
          "severity": {
            "code": "string",
            "name": "string"
          },
          "tripRiskUnit": "quis"
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "TripSegment": [
      {
        "attributes": {
          "agentFees": {
            "amount": "string",
            "currency": "string"
          },
          "arrivalDateTime": "2019-08-24T14:15:22Z",
          "assessment": {
            "code": "string",
            "name": "string"
          },
          "cancelOnly": true,
          "cancellationFees": {
            "amount": "string",
            "currency": "string"
          },
          "carrierName": "string",
          "carrierNumber": "string",
          "departureDateTime": "2019-08-24T14:15:22Z",
          "otherFees": {
            "amount": "string",
            "currency": "string"
          },
          "paidAmount": {
            "amount": "string",
            "currency": "string"
          },
          "portOfDisembarkation": "string",
          "portOfEmbarkation": "string",
          "reasonForCancellation": "string",
          "reasonForDenial": "string",
          "transportType": {
            "code": "string",
            "name": "string"
          }
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "UnverifiedPropertyItem": [
      {
        "attributes": {
          "appraisedValue": {
            "amount": "string",
            "currency": "string"
          },
          "description": "string"
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ],
    "VehicleIncident": [
      {
        "attributes": {
          "airbagsDeployed": true,
          "automationPath": {
            "code": "string",
            "name": "string"
          },
          "childSafetySeatStatus": {
            "code": "string",
            "name": "string"
          },
          "collision": true,
          "collisionPoint": {
            "code": "string",
            "name": "string"
          },
          "damageDescription": "string",
          "driver": "quis",
          "equipmentFailure": true,
          "incidentOwner": "quis",
          "lossParty": {
            "code": "string",
            "name": "string"
          },
          "numOccupants": 0,
          "passengers": [
            "quis"
          ],
          "propertyDamageDescription": "string",
          "propertyValue": {
            "amount": "string",
            "currency": "string"
          },
          "safeToDrive": true,
          "severity": {
            "code": "string",
            "name": "string"
          },
          "theft": true,
          "totalLoss": true,
          "valuationRequired": {
            "code": "string",
            "name": "string"
          },
          "valuationSource": {
            "code": "string",
            "name": "string"
          },
          "vehicle": {
            "color": "string",
            "licensePlate": "string",
            "make": "string",
            "manufacturer": {
              "code": "string",
              "name": "string"
            },
            "model": "string",
            "policySystemId": "string",
            "state": {
              "code": "string",
              "name": "string"
            },
            "style": {
              "code": "string",
              "name": "string"
            },
            "vin": "string",
            "year": 0
          },
          "vehicleDirection": {
            "code": "string",
            "name": "string"
          },
          "vehicleParked": true,
          "vehicleType": {
            "code": "string",
            "name": "string"
          },
          "vehicleUseReason": {
            "code": "string",
            "name": "string"
          }
        },
        "checksum": "string",
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
              "quis"
            ],
            "total": 0
          },
          "property2": {
            "count": 0,
            "data": [
              "quis"
            ],
            "total": 0
          }
        },
        "uri": "string"
      }
    ]
  }
}

response_schema={
  "data": {
    "attributes": {
      "activityPattern": "string",
      "activityType": {
        "code": "string",
        "name": "string"
      },
      "approvalIssue": "string",
      "approvalRationale": "string",
      "approved": true,
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
      "autopilotHandlingDecision": {
        "code": "string",
        "name": "string"
      },
      "autopilotId": "string",
      "autopilotPurpose": {
        "code": "string",
        "name": "string"
      },
      "closeDate": "2019-08-24T14:15:22Z",
      "closeUser": {
        "displayName": "string",
        "id": "string",
        "jsonPath": "string",
        "refid": "string",
        "type": "string",
        "uri": "string"
      },
      "coverageIssues": [
        {
          "coverageSubtype": {
            "code": "string",
            "name": "string"
          },
          "id": "string",
          "reason": "string",
          "severity": {
            "code": "string",
            "name": "string"
          }
        }
      ],
      "createTime": "2019-08-24T14:15:22Z",
      "description": "string",
      "dueDate": "2019-08-24T14:15:22Z",
      "endDate": "2019-08-24T14:15:22Z",
      "escalated": true,
      "escalationDate": "2019-08-24T14:15:22Z",
      "externallyOwned": true,
      "id": "string",
      "importance": {
        "code": "string",
        "name": "string"
      },
      "initialAssignment": {
        "assigneeId": "string",
        "autoAssign": true,
        "claimOwner": true,
        "groupId": "string",
        "name": "string",
        "queueId": "string",
        "userId": "string"
      },
      "mandatory": true,
      "priority": {
        "code": "string",
        "name": "string"
      },
      "recurring": true,
      "relatedTo": {
        "displayName": "string",
        "id": "string",
        "jsonPath": "string",
        "type": "string",
        "uri": "string"
      },
      "startDate": "2019-08-24T14:15:22Z",
      "status": {
        "code": "string",
        "name": "string"
      },
      "subject": "string"
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
  },
  "included": {
    "Assignee": [
      {
        "attributes": {
          "assigneeId": "string",
          "autoAssign": true,
          "claimOwner": true,
          "groupId": "string",
          "name": "string",
          "queueId": "string",
          "userId": "string"
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
    ],
    "Note": [
      {
        "attributes": {
          "author": {
            "displayName": "string",
            "id": "string",
            "jsonPath": "string",
            "refid": "string",
            "type": "string",
            "uri": "string"
          },
          "body": "string",
          "bodySummary": "string",
          "confidential": true,
          "createdDate": "2019-08-24T14:15:22Z",
          "id": "string",
          "relatedTo": {
            "displayName": "string",
            "id": "string",
            "jsonPath": "string",
            "type": "string",
            "uri": "string"
          },
          "securityType": {
            "code": "string",
            "name": "string"
          },
          "subject": "string",
          "topic": {
            "code": "string",
            "name": "string"
          },
          "updateTime": "2019-08-24T14:15:22Z"
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
    ]
  }
}

response_data={
  "data": "activity data",
  "included": {
    "Assignee": [
      {
        "attr":{"assigneeId": "AGT8",
    "autoAssign": true,
    "claimOwner": true,
    "groupId": "Demo",
    "name": "Simple",
    "queueId": "101",
    "userId": "S123"},
    "checksum":"qwertyuiop",
    "id":"004",
    "method":"post"
      }
    ],
    "Note": [
      "STP"
    ]
  }
}