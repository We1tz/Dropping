import asyncio
import re

import asyncpg
from transactions_ml import transactions_model


async def insert_predictions():
    conn = await asyncpg.connect(
        user='we1tz',
        password='a&wU$4NjJeq',
        database='main',
        host='193.187.96.199',
        port='5432'
    )

    results = transactions_model()
    count = 0
    values = []
    for res in results:
        count += 1
        match = re.search(r'\d+\.\d+', str(res))
        if match:
            pred = round(float(match.group()), 4)
            values.append((count, str(pred)))

    # Асинхронная вставка данных
    await conn.executemany("""
        INSERT INTO prediction (id, predict)
        VALUES ($1, $2)
    """, values)

    # Закрытие соединения
    await conn.close()

    print('Выполнено:', f'{count}/{len(results)}')


# Запуск асинхронной функции
asyncio.run(insert_predictions())
