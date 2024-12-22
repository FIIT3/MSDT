import asyncio

import aiohttp


async def get_current_exchange_rate(base_currency: str, target_currency: str) -> None:
    """
    Получает текущий курс обмена валют.
    """
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{base_currency}"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    print(f"Ошибка подключения: {response.status}")
                    return
                data = await response.json()
                if "error" in data:
                    print(f"Ошибка API: {data['error']['message']}")
                else:
                    rates = data.get("conversion_rates", {})
                    rate = rates.get(target_currency)
                    if rate:
                        print(f"Текущий курс {base_currency} -> {target_currency}: {rate}")
                    else:
                        print(f"Курс для {target_currency} не.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


async def main() -> None:
    base_currency = "USD"
    target_currency = input("Введите валюту (например, RUB, BYN): ").strip().upper()
    await get_current_exchange_rate(base_currency, target_currency)


async def get_multiple_rates() -> None:
    '''
    Пример работы
    '''
    tasks = [
        get_current_exchange_rate("USD", "RUB"),
        get_current_exchange_rate("USD", "EUR"),
        get_current_exchange_rate("USD", "JPY"),
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(get_multiple_rates())
