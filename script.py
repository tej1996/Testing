

if __name__ == '__main__':

    list = [['adf','asfaf','fasfsaf,fasf,fsafw','234235','32623gsdgs'],
            ['adawdwd', 'ajfg', 'afwfaw,vadvka,ewtwet', '234245454', '3535fkaugfusgfku'],
            ['lfhliayuio', 'cnbajwg', 'mcasbcui,vradcd,vadvv', '5345335', '3525dsvsdg'],
            ['ckuay', 'irywahfr', 'iwyriqur,vdsve,vdrsttt', '0825684265', '4r23r2rff']]

    for row in list:
        dsids = row[2].split(',')
        i=0
        if len(dsids) > 1:
            for ab in dsids:
                x = row.copy()
                x[2] = ab
                list.insert(i+1,x)
                i=i+1
            list.remove(row)

    for s in list:
        print(s)