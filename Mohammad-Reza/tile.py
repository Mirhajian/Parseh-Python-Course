def kashi(tk, ak, tkh, akh):
    masahat_kashi = tk * ak
    masahat_khooneh = tkh * akh

    tile_count = masahat_khooneh // masahat_kashi

    return tile_count


# tool_kashi = int(input("Enter the tool kashi: "))
# arz_kashi = int(input("Enter the arz kashi: "))

# tool_khooneh = int(input("Enter the tool khooneh: "))
# arz_khooneh = int(input("Enter the arz khooneh: "))

# final = kashi(tool_kashi, arz_kashi, tool_khooneh, arz_khooneh)
# print("The tile count is: ", final)
