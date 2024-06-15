import requests


def queryEmpDataFromROS():
    query = (
        query
    ) = """
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


def queryMinEmpDataFromROS():
    query = (
        query
    ) = """
    query {
        employees {
            nodes {
                email
                firstName
                lastName
                avatarUrl
                slackAvatarUrl
                title
                group
                team
                pod
                hireDate
                type
                status
                remoteStatus
            }
        }
    }
"""
    return query


def get_emp_graphql_data(url, query, token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    data = {
        "query": query,
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    return response.json()["data"]["employees"]["nodes"]
