def mapit(tomap, forward = True):
    mappe = {
    'मुस्तांग' : 'Mustang',
    'पर्वत' : 'Parbat',
    'कास्की' : 'Kaski',
     'म्याग्दी' : 'Myagdi',
     'गोरखा' : 'Gorkha',
     'तनहुँ' : 'Tanahu',
     'स्याङ्जा' : 'Syangja',
     'मनाङ्ग' : 'Manang',
     'नवलपरासी (बर्दघाट सुस्ता पूर्व)' : 'Nawalparasi',
     'बागलुङ' : 'Baglung',
     'लमजुंग' : 'Lamjung',
    }

    if forward == True:
        value = mappe[tomap]
        return value
    else:
        key = [k for k, v in mappe.items() if v == tomap]
        for actual_key in key:
            return actual_key


print(mapit('Kaski', False))

print(mapit('गोरखा'))
    

