n = int(input())

# Thousands
for n1 in range(1, 10):
    # Hundreds
    for n2 in range(1, 10):
        # Tens
        for n3 in range(1, 10):
            # Ones
            for n4 in range(1, 10):
                is_special = n % n1 == 0 and n % n2 == 0 and n % n3 == 0 and n % n4 == 0
                if is_special:
                    print(f"{n1}{n2}{n3}{n4}", end=" ")
