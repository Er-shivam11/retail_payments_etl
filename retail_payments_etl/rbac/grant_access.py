import yaml

def load_roles(file='roles.yaml'):
    with open(file) as f:
        return yaml.safe_load(f)

def grant_access(user_role):
    roles = load_roles()
    access = roles['roles'].get(user_role, {}).get('access', [])
    print(f"Access granted to: {access}")

if __name__ == "__main__":
    grant_access("analyst")
