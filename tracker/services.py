from datetime import timedelta


def classify_task(task, now):

    remaining_time = task.deadline - now

    # Deadline sudah terlewati
    if remaining_time.total_seconds() < 0:
        return "overdue"

    # Deadline kurang dari 24 jam
    if remaining_time < timedelta(hours=24):
        return "approaching"

    # Deadline masih aman
    return "normal"

def sort_tasks(tasks, now):

    for task in tasks:
        task.deadline_category = classify_task(task, now)

    # Tugas mendekati deadline
    approaching = [
        task for task in tasks
        if task.deadline_category == "approaching"
    ]

    # Semua kategori selain approaching
    others = [
        task for task in tasks
        if task.deadline_category != "approaching"
    ]

    # Deadline terdekat berada di atas
    approaching.sort(
        key=lambda task: task.deadline
    )

    # Pertahankan aturan urutan lama untuk sisanya
    others.sort(
        key=lambda task: task.created_at,
        reverse=True
    )

    return approaching + others