import time

import setup
import sortingAlgorithms


print("Setup started")
main_list = setup.ord_list(1, 1_000)
main_list = setup.mix(main_list)
print("Setup complete")
print("Sorting complete")
start_time = time.process_time()
sortingAlgorithms.insertion(main_list)
print("Sorting complete in: ", time.process_time() - start_time)
print("Verification started")
is_sorted = setup.is_truly_sorted(main_list)
print("List is sorted" if is_sorted else "Sorting failed")