import math
import heapq

# Floyd-Warshall Algorithm
def floyd_warshall(matriks_awal, n):
    M = math.inf

    # salin matriks input agar tidak mengubah data asli
    Q = [row[:] for row in matriks_awal]
    R = [[0] * (n + 1) for _ in range(n + 1)] # 0 = tak ada perantara

    # Iterasi untuk setiao titik perantara k
    for k in range(n):
        for i in range(n):
            for j in range(n):
                via_k = Q[i][k] + Q[k][j] # jarak dari i -> j lewat k
                if via_k < Q[i][j]: # jika jarak via k < jarak i -> j
                    # update matriks beban (Q) dan matriks rute (R)
                    Q[i][j] = via_k
                    # Catat titik perantara untuk matriks rute
                    R[i][j] = k if R[k][j] == 0 else R[k][j]

    return Q, R # return... ok

def baca_rute_fw(R, start, end):
    stack = []
    j = end

    # Telusuri ke belakang, kumpulkan semua perantara ke stack
    while R[start][j] != 0:
        stack.append(R[start][j])
        j = R[start][j]

    # Pop stack untuk mendapatkan urutan yang benar
    rute = [start]
    while stack:
        rute.append(stack.pop())
    rute.append(end)
    return rute

# Djikstraaghh shoot-- Algorithm
def dijkstra_matrix(matrix, n, start, end):

    M = math.inf

    Q = [M] * (n + 1)     # Q[i] = jarak terpendek dari start ke i
    R = [0] * (n + 1)     # R[i] = node sebelumnya (untuk rekonstruksi jalur)
    Q[start] = 0

    pq   = [(0, start)]   # priority queue: (jarak, node)
    done = [False] * (n + 1)

    print("=" * 55)
    print(f"ALGORITMA DIJKSTRA: Node {start} ke Node {end}")
    print("=" * 55)

    while pq:
        jarak_min, CN = heapq.heappop(pq)   # CN = Current Node

        if done[CN]:
            continue
        done[CN] = True
        print(f"\nProses Node {CN} | beban min dari asal = {jarak_min}")

        if CN == end:
            print("  → Node tujuan ditemukan, selesai!")
            break

        # Baca baris CN di adjacency matrix untuk temukan tetangga
        for i in range(1, n + 1):
            if matrix[CN][i] != M and not done[i]:
                jarak_baru = Q[CN] + matrix[CN][i]
                if jarak_baru < Q[i]:
                    Q[i] = jarak_baru
                    R[i] = CN                          # catat node sebelumnya
                    heapq.heappush(pq, (jarak_baru, i))
                    print(f"  Update Node {i}: beban min = {jarak_baru}, sebelumnya = {CN}")

    # Rekonstruksi jalur dari matriks R (backtrack dari end ke start)
    jalur = []
    node  = end
    while node != 0:
        jalur.append(node)
        node = R[node]
    jalur.reverse()

    print(f"\n{'=' * 55}")
    if Q[end] == M:
        print(f"Tidak ada jalur dari {start} ke {end}!")
    else:
        print(f"Rute terpendek : {' -> '.join(map(str, jalur))}")
        print(f"Beban minimal  : {int(Q[end])}")

    return Q, R, jalur