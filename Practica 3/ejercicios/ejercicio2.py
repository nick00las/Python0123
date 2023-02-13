def ejercicio2(sentece):
    print("\n** Se está inicializando el ejercicio 2 **")

    # split
    words = sentece.split()
    print("  Se está separando el sentece: ", words, "\n")

    # join
    joined_text = " ".join(words)
    print("  Se está uniendo el sentece: ", joined_text, "\n")

    # count
    occurrence_object = "sentece"
    ocurrence = sentece.count(occurrence_object)
    print(f"  las veces que '{occurrence_object}' aparece: ", ocurrence, "\n")

    # find
    find_object = "imprentas"
    index = sentece.find(find_object)
    print(f"  '{find_object}' fue encontrado en: ", index, "\n")

    # uppercase
    c_letter = sentece.upper()
    print("  el sentece en MAYUSCULAS: ", c_letter, "\n")

    # lowercase
    l_case = sentece.lower()
    print("  el sentece en minusculas: ", l_case, end=" ")

    print("** Acabando el ejercicio 2 **\n")