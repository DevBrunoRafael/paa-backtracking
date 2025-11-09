def solve_partition_memoization(tasks):

    total_load = sum(tasks)
    if total_load % 2 != 0:
        return None

    target_load = total_load // 2
    memo = {}  # Cache para armazenar resultados de (index, current_sum)

    def backtrack_memo(index, current_sum):
        state = (index, current_sum)
        if state in memo:
            return memo[state]  # Retorna resultado já calculado

        if current_sum == target_load:
            return []  # Retorna uma lista vazia para indicar sucesso na busca

        if index >= len(tasks) or current_sum > target_load:
            return None  # Falha

        # Tenta incluir a tarefa atual
        task = tasks[index]
        res = backtrack_memo(index + 1, current_sum + task)
        if res is not None:
            # Sucesso! Adiciona a tarefa atual à solução encontrada na recursão
            memo[state] = [task] + res
            return memo[state]

        # Tenta não incluir a tarefa atual
        res = backtrack_memo(index + 1, current_sum)
        if res is not None:
            memo[state] = res
            return memo[state]

        memo[state] = None  # Marca este estado como sem solução
        return None

    partition1 = backtrack_memo(0, 0)

    # se encontrou uma subconjunto que soma exatamente target_load
    if partition1 is not None:
        partition2 = list(tasks)
        for item in partition1:
            # partition2 contém os elementos restantes (ou seja, as tarefas que não entraram no primeiro subconjunto).
            partition2.remove(item)
        return partition1, partition2
    else:
        # não há solução possível
        return None

# Exemplo de uso
tarefas = [2, 4, 5, 9, 12]
resultado = solve_partition_memoization(tarefas)

if resultado:
    A, B = resultado
    print("Servidor A executa as tarefas:", A, "→ carga =", sum(A))
    print("Servidor B executa as tarefas:", B, "→ carga =", sum(B))
    print("Diferença de carga:", abs(sum(A) - sum(B)))
else:
    print("Não foi possível dividir igualmente as tarefas.")
