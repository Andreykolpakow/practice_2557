# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из
# предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.


res_dict = {}
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        remote_addr, *_ = line.split()
        res_dict[remote_addr] = (res_dict[remote_addr] + 1 if remote_addr in res_dict else 1)

spamers_requests = max(res_dict.values())
for remote_addr, requests in res_dict.items():
    if requests == spamers_requests:
        spamer = remote_addr


print('id спамера:', spamer, '\nколичество запросов:', spamers_requests)