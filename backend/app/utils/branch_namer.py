def make_branch_name(
    team_name: str,
    leader_name: str
):
    team = team_name.upper().replace(" ", "_")

    leader = leader_name.upper().replace(" ", "_")

    return f"{team}_{leader}_AI_Fix"