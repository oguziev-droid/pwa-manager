from .models import PWAApplication


def deduplicate(
    applications: list[PWAApplication],
) -> list[PWAApplication]:

    groups = {}

    for app in applications:

        key = app.normalized_name

        if key not in groups:
            groups[key] = []

        groups[key].append(app)


    result = []

    for name, apps in groups.items():

        # пріоритет:
        # managed > chrome

        selected = sorted(
            apps,
            key=lambda x:
                0 if x.source == "managed"
                else 1
        )[0]

        result.append(selected)

    return result
