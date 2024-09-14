    def post(self, request):
        if 'check1' in request.POST:
            if 'check2' in request.POST:
                if 'check3' in request.POST:
                    if 'check4' in request.POST:
                        if 'check5' in request.POST:
                            if 'check6' in request.POST:
                                if 'check7' in request.POST:
                                    if 'check8' in request.POST:
                        else:
                            self.params['checked1'] = '2'
                            self.params['checked2'] = None
                            self.params['checked3'] = None
                            self.params['checked4'] = None
                    else:
                        self.params['checked1'] = '1.5'
                        self.params['checked2'] = None
                        self.params['checked3'] = None
                else:
                    self.params['checked1'] = '1'
                    self.params['checked2'] = None
            else:
                self.params['checked1'] = '0.5'
                self.params['checked2'] = '0'
                if 'check3' in request.POST:
                    if 'check4' in request.POST:
                        if 'check5' in request.POST:
                        else:
                            self.params['checked3'] = '1'
                            self.params['checked4'] = None
                    else:
                        self.params['checked3'] = '0.5'
                        self.params['checked4'] = '0'
                else:
                    self.params['checked3'] = '0'
                    if 'check4' in request.POST:






for i in list:
    if list[i] == True & list[i+1] == True :
        continue
    if list[i] == False:
        list[i] = '0'
    if list[i] == True:
        if list[i-1] == '0':
            list[i] = '0.5'
        if list[i-1] == True & list[i-2] == '0':
            list[i-1] = '1'
            list[i] == None
        if list[i-1] == True & list[i-2] == True & list[i-3] == '0':
            list[i-2] == '1.5'
            list[i-1] == None
            list[i] == None
        if list[i-1] == True & list[i-2] == True & list[i-3] == True & list[i-4] == '0':
            list[i-3] == '2'
            list[i-2] == None
            list[i-1] == None
            list[i] == None
        if list[i-1] == True & list[i-2] == True & list[i-3] == True & list[i-4] == True & list[i-5] == '0':
            list[i-4] == '2.5'
            list[i-3] == None
            list[i-2] == None
            list[i-1] == None
            list[i] == None
        if list[i-1] == True & list[i-2] == True & list[i-3] == True & list[i-4] == True & list[i-5] == True & list[i-6] == '0':
            list[i-5] = '3'
            list[i-4] = None
            list[i-3] = None
            list[i-2] = None
            list[i-1] = None
            list[i] = None
        if list[i-1] == True & list[i-2] == True & list[i-3] == True & list[i-4] == True & list[i-5] == True & list[i-6] == True & list[i-7] == '0':
            list[i-6] = '3.5'
            list[i-5] = None
            list[i-4] = None
            list[i-3] = None
            list[i-2] = None
            list[i-1] = None
            list[i] = None
        if list[i-1] == True & list[i-2] == True & list[i-3] == True & list[i-4] == True & list[i-5] == True & list[i-6] == True & list[i-7] == True  & list[i-8] == '0':
            list[i-7] = '4'
            list[i-6] = None
            list[i-5] = None
            list[i-4] = None
            list[i-3] = None
            list[i-2] = None
            list[i-1] = None
            list[i] = None

        
if 'check2' in request.POST:
            if self.params['result'] is None:
                self.params['result'] = ''
            self.params['result'] += 'checked2 '
            self.params['ch2'] = 'Tru'

for i in 32:
    if 'checki' in request.POST:
        self.params['chi'] = 'Tru'