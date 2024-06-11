def getEmpDataFromROS():
    query = query = """
    query {
        employees {
            nodes {
                ...minEmployeeInfo
                groupId
                teamId
                podId
                pronouns
                slackId
                slackHandle
                githubCloudUsername
                githubEnterpriseUsername
                building
                floor
                seat
                id
                hireDate
                type
                status
                timeType
                jobFamily0
                jobFamily1
                jobFamily2
                jobFamily3
                jobProfileStartDate
                remoteStatus
                officeLocation
                locationCity
                locationState
                locationCountry
                managerDirectEmployee {
                    ...minEmployeeInfo
                }
                managerDlevelEmployee {
                    ...minEmployeeInfo
                }
                managerVlevelEmployee {
                    ...minEmployeeInfo
                }
                managerClevelEmployee {
                    ...minEmployeeInfo
                }
                directReports {
                    ...minEmployeeInfo
                }
            }
        }
    }

    fragment minEmployeeInfo on Employee {
        email
        firstName
        lastName
        avatarUrl
        slackAvatarUrl
        title
        group
        team
        pod
    }
"""


    return query