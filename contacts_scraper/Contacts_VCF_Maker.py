import vobject


def vcf_maker():
    rew_numbers_list = []

    text_file_name_to_vcf = input("Enter the text file name\n >")
    vcf_file_name_to_save = input("Enter the vcf file name\n >")
    numbers_name = input("Enter a sample name for each contact\n >")
    try:
        with open(
            f"{text_file_name_to_vcf}.txt", "r+", encoding="utf-8"
        ) as numbers_text_file:
            read_the_file = numbers_text_file.readlines()
            for each_number in read_the_file:
                raw_number = each_number.replace(" ", "")
                print(raw_number)
                if raw_number not in rew_numbers_list:
                    rew_numbers_list.append(raw_number.rstrip("\n"))
        for numbers_in_list in rew_numbers_list:
            index_of_items = rew_numbers_list.index(numbers_in_list)
            person = {
                "n": f"{numbers_name}_{index_of_items+1}",
                "tel": numbers_in_list,
            }

            vcard = vobject.readOne("\n".join([f"{k}:{v}" for k, v in person.items()]))
            vcard.name = "VCARD"
            vcard.useBegin = True
            vcard.prettyPrint()

            with open(f"{vcf_file_name_to_save}.vcf", "a+", newline="") as f:
                f.write(vcard.serialize())

    except:
        print("File doesn't found!")
