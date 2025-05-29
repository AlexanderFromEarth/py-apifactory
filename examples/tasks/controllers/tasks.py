tasks = {}
last_id = 0


async def get_tasks(_):
    return [*tasks.values()]


async def create_task(params):
    global last_id

    last_id += 1
    tasks[last_id] = {**params['body'], 'id': last_id}

    return last_id


async def get_task(params):
    return tasks[params['taskId']]


async def update_task(params):
    task = tasks[params['taskId']]

    if 'title' in params['body']:
        task['title'] = params['body']['title']
    if 'description' in params['body']:
        task['description'] = params['body']['description']


async def delete_task(params):
    del tasks[params['taskId']]
