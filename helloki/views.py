import os
import time
from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView
import ffmpeg
import glob
from .forms import HelloForm
import subprocess
import pandas as pd
from sklearn import tree
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

class HelloViewki(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'コード伴奏自動生成アプリ',
            'message': 'your data:',
            'form': HelloForm(),
            'result': '',
            'checked': False,
            **{f'chug{i}': 'Fal' for i in range(1, 65)},
            **{f'chugf{i}': 'Fal' for i in range(1, 65)},
            **{f'chuf{i}': 'Fal' for i in range(1, 65)},
            **{f'chue{i}': 'Fal' for i in range(1, 65)},
            **{f'chuef{i}': 'Fal' for i in range(1, 65)},
            **{f'chud{i}': 'Fal' for i in range(1, 65)},
            **{f'chudf{i}': 'Fal' for i in range(1, 65)},
            **{f'ch{i}': 'Fal' for i in range(1, 65)},
            **{f'chb{i}': 'Fal' for i in range(1, 65)},
            **{f'chbf{i}': 'Fal' for i in range(1, 65)},
            **{f'cha{i}': 'Fal' for i in range(1, 65)},
            **{f'chaf{i}': 'Fal' for i in range(1, 65)},
            **{f'chg{i}': 'Fal' for i in range(1, 65)},
            **{f'chgf{i}': 'Fal' for i in range(1, 65)},
            **{f'chf{i}': 'Fal' for i in range(1, 65)},
            **{f'che{i}': 'Fal' for i in range(1, 65)},
            **{f'chef{i}': 'Fal' for i in range(1, 65)},
            **{f'chd{i}': 'Fal' for i in range(1, 65)},
            **{f'chdf{i}': 'Fal' for i in range(1, 65)},
            **{f'chc{i}': 'Fal' for i in range(1, 65)},
            **{f'chdb{i}': 'Fal' for i in range(1, 65)},
            **{f'chdbf{i}': 'Fal' for i in range(1, 65)},
            **{f'chda{i}': 'Fal' for i in range(1, 65)},
            **{f'chdaf{i}': 'Fal' for i in range(1, 65)},
            **{f'chdg{i}': 'Fal' for i in range(1, 65)},
            **{f'chk{i}': 'Fal' for i in range(1, 65)},
            'codename1':'mi',
            'codename2':'mi',
            'codename3':'mi',
            'codename4':'mi',
            'codename5':'mi',
            'codename6':'mi',
            'codename7':'mi',
            'codename8':'mi',
            'codename9':'mi',
            'codename10':'mi',
            'codename11':'mi',
            'codename12':'mi',
            'codename13':'mi',
            'codename14':'mi',
            'codename15':'mi',
            'codename16':'mi',
            'colist':'s',
            'ch1a': False,
            'audio_url': None,
            'audiocode_url':None,
            'audiofull_url':None,
            'datacsv':'mmm',
            'kicode':'mmm',
            'timea':None,
            'timek':None,
        }

    def get(self, request):
        return render(request, 'helloki/indexki.html', self.params)

    def post(self, request):
        print("Form submitted!")  # フォームが送信されたことを確認するためのログ

        form = HelloForm(request.POST)
        if form.is_valid():
            # フォームデータを処理する
            self.params['form'] = form
            

        # チェックボックスの状態を更新,4syousetu
        for i in range(1, 65):
            check_key = f'check{i}'
            chi_key = f'ch{i}'
            if check_key in request.POST:
                self.params[chi_key] = 'Tru'
            else:
                self.params[chi_key] = 'Fal'

        for i in range(1, 65):
            check_keyk = f'checkk{i}'
            chi_keyk = f'chk{i}'
            if check_keyk in request.POST:
                self.params[chi_keyk] = 'Tru'
            else:
                self.params[chi_keyk] = 'Fal'

        for i in range(1, 65):
            check_keyugf = f'checkugf{i}'
            chi_keyugf = f'chugf{i}'
            if check_keyugf in request.POST:
                self.params[chi_keyugf] = 'Tru'
            else:
                self.params[chi_keyugf] = 'Fal'

        for i in range(1, 65):
            check_keyuf = f'checkuf{i}'
            chi_keyuf = f'chuf{i}'
            if check_keyuf in request.POST:
                self.params[chi_keyuf] = 'Tru'
            else:
                self.params[chi_keyuf] = 'Fal'

        for i in range(1, 65):
            check_keyue = f'checkue{i}'
            chi_keyue = f'chue{i}'
            if check_keyue in request.POST:
                self.params[chi_keyue] = 'Tru'
            else:
                self.params[chi_keyue] = 'Fal'

        for i in range(1, 65):
            check_keyuef = f'checkuef{i}'
            chi_keyuef = f'chuef{i}'
            if check_keyuef in request.POST:
                self.params[chi_keyuef] = 'Tru'
            else:
                self.params[chi_keyuef] = 'Fal'

        for i in range(1, 65):
            check_keyud = f'checkud{i}'
            chi_keyud = f'chud{i}'
            if check_keyud in request.POST:
                self.params[chi_keyud] = 'Tru'
            else:
                self.params[chi_keyud] = 'Fal'

        for i in range(1, 65):
            check_keyudf = f'checkudf{i}'
            chi_keyudf = f'chudf{i}'
            if check_keyudf in request.POST:
                self.params[chi_keyudf] = 'Tru'
            else:
                self.params[chi_keyudf] = 'Fal'



        for i in range(1, 65):
            check_keyb = f'checkb{i}'
            chi_keyb = f'chb{i}'
            if check_keyb in request.POST:
                self.params[chi_keyb] = 'Tru'
            else:
                self.params[chi_keyb] = 'Fal'

        for i in range(1, 65):
            check_keybf = f'checkbf{i}'
            chi_keybf = f'chbf{i}'
            if check_keybf in request.POST:
                self.params[chi_keybf] = 'Tru'
            else:
                self.params[chi_keybf] = 'Fal'

        for i in range(1, 65):
            check_keya = f'checka{i}'
            chi_keya = f'cha{i}'
            if check_keya in request.POST:
                self.params[chi_keya] = 'Tru'
            else:
                self.params[chi_keya] = 'Fal'

        for i in range(1, 65):
            check_keyaf = f'checkaf{i}'
            chi_keyaf = f'chaf{i}'
            if check_keyaf in request.POST:
                self.params[chi_keyaf] = 'Tru'
            else:
                self.params[chi_keyaf] = 'Fal'

        for i in range(1, 65):
            check_keyg = f'checkg{i}'
            chi_keyg = f'chg{i}'
            if check_keyg in request.POST:
                self.params[chi_keyg] = 'Tru'
            else:
                self.params[chi_keyg] = 'Fal'

        for i in range(1, 65):
            check_keygf = f'checkgf{i}'
            chi_keygf = f'chgf{i}'
            if check_keygf in request.POST:
                self.params[chi_keygf] = 'Tru'
            else:
                self.params[chi_keygf] = 'Fal'

        for i in range(1, 65):
            check_keyf = f'checkf{i}'
            chi_keyf = f'chf{i}'
            if check_keyf in request.POST:
                self.params[chi_keyf] = 'Tru'
            else:
                self.params[chi_keyf] = 'Fal'

        for i in range(1, 65):
            check_keye = f'checke{i}'
            chi_keye = f'che{i}'
            if check_keye in request.POST:
                self.params[chi_keye] = 'Tru'
            else:
                self.params[chi_keye] = 'Fal'

        for i in range(1, 65):
            check_keyef = f'checkef{i}'
            chi_keyef = f'chef{i}'
            if check_keyef in request.POST:
                self.params[chi_keyef] = 'Tru'
            else:
                self.params[chi_keyef] = 'Fal'

        for i in range(1, 65):
            check_keyd = f'checkd{i}'
            chi_keyd = f'chd{i}'
            if check_keyd in request.POST:
                self.params[chi_keyd] = 'Tru'
            else:
                self.params[chi_keyd] = 'Fal'

        for i in range(1, 65):
            check_keydf = f'checkdf{i}'
            chi_keydf = f'chdf{i}'
            if check_keydf in request.POST:
                self.params[chi_keydf] = 'Tru'
            else:
                self.params[chi_keydf] = 'Fal'

        for i in range(1, 65):
            check_keyc = f'checkc{i}'
            chi_keyc = f'chc{i}'
            if check_keyc in request.POST:
                self.params[chi_keyc] = 'Tru'
            else:
                self.params[chi_keyc] = 'Fal'

        for i in range(1, 65):
            check_keydb = f'checkdb{i}'
            chi_keydb = f'chdb{i}'
            if check_keydb in request.POST:
                self.params[chi_keydb] = 'Tru'
            else:
                self.params[chi_keydb] = 'Fal'

        for i in range(1, 65):
            check_keydbf = f'checkdbf{i}'
            chi_keydbf = f'chdbf{i}'
            if check_keydbf in request.POST:
                self.params[chi_keydbf] = 'Tru'
            else:
                self.params[chi_keydbf] = 'Fal'

        for i in range(1, 65):
            check_keyda = f'checkda{i}'
            chi_keyda = f'chda{i}'
            if check_keyda in request.POST:
                self.params[chi_keyda] = 'Tru'
            else:
                self.params[chi_keyda] = 'Fal'

        for i in range(1, 65):
            check_keydaf = f'checkdaf{i}'
            chi_keydaf = f'chdaf{i}'
            if check_keydaf in request.POST:
                self.params[chi_keydaf] = 'Tru'
            else:
                self.params[chi_keydaf] = 'Fal'

        for i in range(1, 65):
            check_keydg = f'checkdg{i}'
            chi_keydg = f'chdg{i}'
            if check_keydg in request.POST:
                self.params[chi_keydg] = 'Tru'
            else:
                self.params[chi_keydg] = 'Fal'



        #メロ音源リスト
        s_pathsug = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ug0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ug1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ug1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ug2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ug2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ug3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ug3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ug4.mp3'),
        ]

        for path in s_pathsug:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")

        s_pathsugf = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ugf0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ugf1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ugf1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ugf2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ugf2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ugf3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ugf3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ugf4.mp3'),
        ]

        for path in s_pathsugf:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")


        s_pathsuf = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'uf0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'uf1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'uf1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'uf2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'uf2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'uf3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'uf3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'uf4.mp3'),
        ]

        for path in s_pathsuf:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")

        s_pathsue = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ue0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ue1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ue1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ue2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ue2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ue3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ue3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ue4.mp3'),
        ]

        for path in s_pathsue:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")


        s_pathsuef = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'uef0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'uef1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'uef1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'uef2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'uef2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'uef3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'uef3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'uef4.mp3'),
        ]

        for path in s_pathsuef:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")

        s_pathsud = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ud0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ud1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ud1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ud2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ud2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ud3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ud3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ud4.mp3'),
        ]

        for path in s_pathsud:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")

        s_pathsudf = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'udf0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'udf1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'udf1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'udf2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'udf2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'udf3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'udf3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'udf4.mp3'),
        ]

        for path in s_pathsudf:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")

        s_paths = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's4.mp3'),
        ]

        for path in s_paths:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")
            
        s_pathsb = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'b0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'b1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'b1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'b2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'b2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'b3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'b3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'b4.mp3'),
        ]

        for path in s_pathsb:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")
            
        s_pathsbf = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'bf0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'bf1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'bf1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'bf2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'bf2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'bf3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'bf3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'bf4.mp3'),
        ]

        for path in s_pathsbf:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")
            
        s_pathsa = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'a0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'a1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'a1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'a2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'a2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'a3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'a3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'a4.mp3'),
        ]

        for path in s_pathsa:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")
            
        s_pathsaf = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'af0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'af1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'af1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'af2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'af2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'af3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'af3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'af4.mp3'),
        ]

        for path in s_pathsaf:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")
            
        s_pathsg = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'g0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'g1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'g1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'g2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'g2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'g3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'g3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'g4.mp3'),
        ]

        for path in s_pathsg:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")
            
        s_pathsgf = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'gf0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'gf1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'gf1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'gf2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'gf2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'gf3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'gf3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'gf4.mp3'),
        ]

        for path in s_pathsgf:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")
            
        s_pathsf = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'f0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'f1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'f1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'f2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'f2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'f3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'f3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'f4.mp3'),
        ]

        for path in s_pathsf:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")
            
        s_pathse = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'e0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'e1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'e1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'e2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'e2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'e3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'e3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'e4.mp3'),
        ]

        for path in s_pathse:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")
            
        s_pathsef = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ef0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ef1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ef1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ef2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ef2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ef3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ef3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'ef4.mp3'),
        ]

        for path in s_pathsef:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")
            
        s_pathsd = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'd0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'd1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'd1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'd2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'd2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'd3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'd3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'd4.mp3'),
        ]

        for path in s_pathsd:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")
            
        s_pathsdf = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'df0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'df1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'df1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'df2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'df2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'df3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'df3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'df4.mp3'),
        ]

        for path in s_pathsdf:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")
            
        s_pathsc = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'c0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'c1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'c1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'c2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'c2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'c3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'c3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'c4.mp3'),
        ]

        for path in s_pathsc:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")
            
        s_pathsdb = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'db0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'db1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'db1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'db2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'db2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'db3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'db3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'db4.mp3'),
        ]

        for path in s_pathsdb:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")
            
        s_pathsdbf = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'dbf0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'dbf1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'dbf1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'dbf2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'dbf2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'dbf3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'dbf3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'dbf4.mp3'),
        ]

        for path in s_pathsdbf:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")
            
        s_pathsda = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'da0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'da1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'da1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'da2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'da2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'da3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'da3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'da4.mp3'),
        ]

        for path in s_pathsda:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")
            
        s_pathsdaf = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'daf0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'daf1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'daf1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'daf2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'daf2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'daf3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'daf3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'daf4.mp3'),
        ]

        for path in s_pathsdaf:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")
            
        s_pathsdg = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 's0.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'dg0.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'dg1.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'dg1.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'dg2.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'dg2.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'dg3.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'dg3.5.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'dg4.mp3'),
        ]

        for path in s_pathsdg:
            if not os.path.exists(path):
                raise FileNotFoundError(f"The file {path} does not exist.")
            
        




        #チェックリスト、4小節ぶん

        a_listug = [self.params[f'chug{i}'] for i in range(1, 65)]

        a_listugf = [self.params[f'chugf{i}'] for i in range(1, 65)]

        a_listuf = [self.params[f'chuf{i}'] for i in range(1, 65)]

        a_listue = [self.params[f'chue{i}'] for i in range(1, 65)]

        a_listuef = [self.params[f'chuef{i}'] for i in range(1, 65)]

        a_listud = [self.params[f'chud{i}'] for i in range(1, 65)]

        a_listudf = [self.params[f'chudf{i}'] for i in range(1, 65)]

        a_list = [self.params[f'ch{i}'] for i in range(1, 65)]

        a_listk = [self.params[f'chk{i}'] for i in range(1, 65)]

        a_listb = [self.params[f'chb{i}'] for i in range(1, 65)]

        a_listbf = [self.params[f'chbf{i}'] for i in range(1, 65)]

        a_lista = [self.params[f'cha{i}'] for i in range(1, 65)]

        a_listaf = [self.params[f'chaf{i}'] for i in range(1, 65)]

        a_listg = [self.params[f'chg{i}'] for i in range(1, 65)]

        a_listgf = [self.params[f'chgf{i}'] for i in range(1, 65)]

        a_listf = [self.params[f'chf{i}'] for i in range(1, 65)]

        a_liste = [self.params[f'che{i}'] for i in range(1, 65)]

        a_listef = [self.params[f'chef{i}'] for i in range(1, 65)]

        a_listd = [self.params[f'chd{i}'] for i in range(1, 65)]

        a_listdf = [self.params[f'chdf{i}'] for i in range(1, 65)]

        a_listc = [self.params[f'chc{i}'] for i in range(1, 65)]

        a_listdb = [self.params[f'chdb{i}'] for i in range(1, 65)]

        a_listdbf = [self.params[f'chdbf{i}'] for i in range(1, 65)]

        a_listda = [self.params[f'chda{i}'] for i in range(1, 65)]

        a_listdaf = [self.params[f'chdaf{i}'] for i in range(1, 65)]

        a_listdg = [self.params[f'chdg{i}'] for i in range(1, 65)]



        #最終リスト、4小節ぶん
        f_list = ['Fal'] * 64


        # ファイルパスの整理とNoneの取り除き
        for i in range(len(a_list)):
            if a_list[i] == 'Tru':
                if i + 1 < len(a_list) and a_list[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsa[1]
                        elif a_list[i - 1] == 'Fal':
                            f_list[i] = s_pathsa[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_list[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsa[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsa[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsa[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsa[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsa[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsa[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsa[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsa[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_paths[1]
                elif a_list[i - 1] == 'Fal':
                    f_list[i] = s_paths[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_list[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_paths[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_paths[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_paths[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_paths[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_paths[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_paths[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_paths[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_paths[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listug[i] == 'Tru':
                if i + 1 < len(a_list) and a_listug[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsug[1]
                        elif a_listug[i - 1] == 'Fal':
                            f_list[i] = s_pathsug[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listug[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsug[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsug[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsug[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsug[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsug[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsug[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsug[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsug[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsug[1]
                elif a_listug[i - 1] == 'Fal':
                    f_list[i] = s_pathsug[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listug[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsug[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsug[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsug[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsug[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsug[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsug[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsug[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsug[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listugf[i] == 'Tru':
                if i + 1 < len(a_list) and a_listugf[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsugf[1]
                        elif a_listugf[i - 1] == 'Fal':
                            f_list[i] = s_pathsugf[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listugf[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsugf[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsugf[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsugf[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsugf[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsugf[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsugf[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsugf[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsugf[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsugf[1]
                elif a_listugf[i - 1] == 'Fal':
                    f_list[i] = s_pathsugf[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listugf[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsugf[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsugf[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsugf[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsugf[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsugf[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsugf[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsugf[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsugf[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listuf[i] == 'Tru':
                if i + 1 < len(a_list) and a_listuf[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsuf[1]
                        elif a_listuf[i - 1] == 'Fal':
                            f_list[i] = s_pathsuf[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listuf[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsuf[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsuf[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsuf[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsuf[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsuf[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsuf[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsuf[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsuf[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsuf[1]
                elif a_listuf[i - 1] == 'Fal':
                    f_list[i] = s_pathsuf[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listuf[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsuf[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsuf[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsuf[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsuf[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsuf[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsuf[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsuf[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsuf[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listue[i] == 'Tru':
                if i + 1 < len(a_list) and a_listue[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsue[1]
                        elif a_listue[i - 1] == 'Fal':
                            f_list[i] = s_pathsue[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listue[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsue[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsue[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsue[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsue[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsue[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsue[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsue[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsue[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsue[1]
                elif a_listue[i - 1] == 'Fal':
                    f_list[i] = s_pathsue[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listue[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsue[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsue[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsue[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsue[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsue[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsue[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsue[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsue[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listuef[i] == 'Tru':
                if i + 1 < len(a_list) and a_listuef[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsuef[1]
                        elif a_listuef[i - 1] == 'Fal':
                            f_list[i] = s_pathsuef[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listuef[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsuef[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsuef[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsuef[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsuef[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsuef[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsuef[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsuef[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsuef[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsuef[1]
                elif a_listuef[i - 1] == 'Fal':
                    f_list[i] = s_pathsuef[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listuef[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsuef[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsuef[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsuef[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsuef[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsuef[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsuef[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsuef[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsuef[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listud[i] == 'Tru':
                if i + 1 < len(a_list) and a_listud[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsud[1]
                        elif a_listud[i - 1] == 'Fal':
                            f_list[i] = s_pathsud[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listud[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsud[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsud[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsud[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsud[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsud[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsud[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsud[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsud[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsud[1]
                elif a_listud[i - 1] == 'Fal':
                    f_list[i] = s_pathsud[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listud[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsud[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsud[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsud[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsud[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsud[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsud[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsud[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsud[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listudf[i] == 'Tru':
                if i + 1 < len(a_list) and a_listudf[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsudf[1]
                        elif a_listudf[i - 1] == 'Fal':
                            f_list[i] = s_pathsudf[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listudf[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsudf[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsudf[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsudf[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsudf[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsudf[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsudf[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsudf[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsudf[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsudf[1]
                elif a_listudf[i - 1] == 'Fal':
                    f_list[i] = s_pathsudf[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listudf[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsudf[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsudf[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsudf[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsudf[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsudf[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsudf[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsudf[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsudf[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listb[i] == 'Tru':
                if i + 1 < len(a_list) and a_listb[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsb[1]
                        elif a_listb[i - 1] == 'Fal':
                            f_list[i] = s_pathsb[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listb[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsb[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsb[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsb[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsb[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsb[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsb[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsb[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsb[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsb[1]
                elif a_listb[i - 1] == 'Fal':
                    f_list[i] = s_pathsb[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listb[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsb[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsb[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsb[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsb[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsb[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsb[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsb[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsb[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listbf[i] == 'Tru':
                if i + 1 < len(a_list) and a_listbf[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsbf[1]
                        elif a_listbf[i - 1] == 'Fal':
                            f_list[i] = s_pathsbf[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listbf[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsbf[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsbf[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsbf[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsbf[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsbf[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsbf[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsbf[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsbf[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsbf[1]
                elif a_listbf[i - 1] == 'Fal':
                    f_list[i] = s_pathsbf[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listbf[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsbf[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsbf[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsbf[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsbf[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsbf[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsbf[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsbf[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsbf[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_lista[i] == 'Tru':
                if i + 1 < len(a_list) and a_lista[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsa[1]
                        elif a_lista[i - 1] == 'Fal':
                            f_list[i] = s_pathsa[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_lista[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsa[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsa[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsa[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsa[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsa[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsa[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsa[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsa[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsa[1]
                elif a_lista[i - 1] == 'Fal':
                    f_list[i] = s_pathsa[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_lista[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsa[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsa[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsa[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsa[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsa[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsa[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsa[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsa[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listaf[i] == 'Tru':
                if i + 1 < len(a_list) and a_listaf[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsaf[1]
                        elif a_listaf[i - 1] == 'Fal':
                            f_list[i] = s_pathsaf[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listaf[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsaf[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsaf[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsaf[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsaf[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsaf[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsaf[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsaf[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsaf[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsaf[1]
                elif a_listaf[i - 1] == 'Fal':
                    f_list[i] = s_pathsaf[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listaf[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsaf[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsaf[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsaf[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsaf[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsaf[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsaf[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsaf[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsaf[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listg[i] == 'Tru':
                if i + 1 < len(a_list) and a_listg[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsg[1]
                        elif a_listg[i - 1] == 'Fal':
                            f_list[i] = s_pathsg[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listg[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsg[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsg[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsg[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsg[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsg[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsg[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsg[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsg[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsg[1]
                elif a_listg[i - 1] == 'Fal':
                    f_list[i] = s_pathsg[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listg[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsg[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsg[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsg[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsg[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsg[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsg[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsg[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsg[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listgf[i] == 'Tru':
                if i + 1 < len(a_list) and a_listgf[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsgf[1]
                        elif a_listgf[i - 1] == 'Fal':
                            f_list[i] = s_pathsgf[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listgf[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsgf[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsgf[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsgf[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsgf[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsgf[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsgf[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsgf[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsgf[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsgf[1]
                elif a_listgf[i - 1] == 'Fal':
                    f_list[i] = s_pathsgf[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listgf[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsgf[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsgf[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsgf[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsgf[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsgf[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsgf[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsgf[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsgf[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listf[i] == 'Tru':
                if i + 1 < len(a_list) and a_listf[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsf[1]
                        elif a_listf[i - 1] == 'Fal':
                            f_list[i] = s_pathsf[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listf[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsf[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsf[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsf[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsf[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsf[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsf[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsf[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsf[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsf[1]
                elif a_listf[i - 1] == 'Fal':
                    f_list[i] = s_pathsf[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listf[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsf[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsf[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsf[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsf[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsf[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsf[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsf[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsf[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_liste[i] == 'Tru':
                if i + 1 < len(a_list) and a_liste[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathse[1]
                        elif a_liste[i - 1] == 'Fal':
                            f_list[i] = s_pathse[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_liste[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathse[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathse[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathse[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathse[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathse[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathse[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathse[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_paths[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathse[1]
                elif a_liste[i - 1] == 'Fal':
                    f_list[i] = s_pathse[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_liste[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathse[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathse[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathse[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathse[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathse[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathse[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathse[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathse[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listef[i] == 'Tru':
                if i + 1 < len(a_list) and a_listef[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsef[1]
                        elif a_listef[i - 1] == 'Fal':
                            f_list[i] = s_pathsef[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listef[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsef[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsef[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsef[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsef[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsef[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsef[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsef[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsef[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsef[1]
                elif a_listef[i - 1] == 'Fal':
                    f_list[i] = s_pathsef[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listef[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsef[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsef[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsef[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsef[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsef[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsef[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsef[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsef[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listd[i] == 'Tru':
                if i + 1 < len(a_list) and a_listd[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsd[1]
                        elif a_listd[i - 1] == 'Fal':
                            f_list[i] = s_pathsd[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listd[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsd[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsd[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsd[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsd[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsd[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsd[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsd[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsd[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsd[1]
                elif a_listd[i - 1] == 'Fal':
                    f_list[i] = s_pathsd[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listd[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsd[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsd[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsd[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsd[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsd[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsd[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsd[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsd[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listdf[i] == 'Tru':
                if i + 1 < len(a_list) and a_listdf[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsdf[1]
                        elif a_listdf[i - 1] == 'Fal':
                            f_list[i] = s_pathsdf[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listdf[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsdf[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsdf[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsdf[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsdf[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsdf[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsdf[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsdf[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsdf[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsdf[1]
                elif a_listdf[i - 1] == 'Fal':
                    f_list[i] = s_pathsdf[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listdf[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsdf[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsdf[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsdf[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsdf[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsdf[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsdf[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsdf[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsdf[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listc[i] == 'Tru':
                if i + 1 < len(a_list) and a_listc[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsc[1]
                        elif a_listc[i - 1] == 'Fal':
                            f_list[i] = s_pathsc[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listc[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsc[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsc[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsc[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsc[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsc[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsc[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsc[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsc[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsc[1]
                elif a_listc[i - 1] == 'Fal':
                    f_list[i] = s_pathsc[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listc[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsc[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsc[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsc[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsc[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsc[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsc[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsc[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsc[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listdb[i] == 'Tru':
                if i + 1 < len(a_list) and a_listdb[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsdb[1]
                        elif a_listdb[i - 1] == 'Fal':
                            f_list[i] = s_pathsdb[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listdb[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsdb[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsdb[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsdb[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsdb[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsdb[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsdb[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsdb[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsdb[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsdb[1]
                elif a_listdb[i - 1] == 'Fal':
                    f_list[i] = s_pathsdb[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listdb[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsdb[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsdb[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsdb[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsdb[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsdb[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsdb[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsdb[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsdb[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listdbf[i] == 'Tru':
                if i + 1 < len(a_list) and a_listdbf[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsdbf[1]
                        elif a_listdbf[i - 1] == 'Fal':
                            f_list[i] = s_pathsdbf[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listdbf[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsdbf[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsdbf[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsdbf[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsdbf[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsdbf[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsdbf[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsdbf[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsdbf[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsdbf[1]
                elif a_listdbf[i - 1] == 'Fal':
                    f_list[i] = s_pathsdbf[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listdbf[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsdbf[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsdbf[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsdbf[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsdbf[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsdbf[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsdbf[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsdbf[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsdbf[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listda[i] == 'Tru':
                if i + 1 < len(a_list) and a_listda[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsda[1]
                        elif a_listda[i - 1] == 'Fal':
                            f_list[i] = s_pathsda[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listda[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsda[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsda[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsda[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsda[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsda[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsda[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsda[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsda[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsda[1]
                elif a_listda[i - 1] == 'Fal':
                    f_list[i] = s_pathsda[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listda[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsda[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsda[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsda[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsda[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsda[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsda[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsda[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsda[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listdaf[i] == 'Tru':
                if i + 1 < len(a_list) and a_listdaf[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsdaf[1]
                        elif a_listdaf[i - 1] == 'Fal':
                            f_list[i] = s_pathsdaf[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listdaf[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsdaf[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsdaf[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsdaf[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsdaf[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsdaf[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsdaf[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsdaf[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsdaf[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsdaf[1]
                elif a_listdaf[i - 1] == 'Fal':
                    f_list[i] = s_pathsdaf[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listdaf[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsdaf[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsdaf[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsdaf[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsdaf[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsdaf[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsdaf[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsdaf[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsdaf[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            elif a_listdg[i] == 'Tru':
                if i + 1 < len(a_list) and a_listdg[i + 1] == 'Tru':
                    if a_listk[i + 1] == 'Tru':
                        if i == 0:
                            f_list[i] = s_pathsdg[1]
                        elif a_listdg[i - 1] == 'Fal':
                            f_list[i] = s_pathsdg[1]
                        else:
                            count_tru = 0
                            j = i
                            while j >= 0 and a_listdg[j] == 'Tru':
                                count_tru += 1
                                j -= 1
            
                            if count_tru == 1:
                                f_list[i] = s_pathsdg[1]
                            elif count_tru == 2:
                                f_list[i - 1] = s_pathsdg[2]
                                f_list[i] = 'Non'
                            elif count_tru == 3:
                                f_list[i - 2] = s_pathsdg[3]
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 4:
                                f_list[i - 3] = s_pathsdg[4]
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 5:
                                f_list[i - 4] = s_pathsdg[5]
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 6:
                                f_list[i - 5] = s_pathsdg[6]
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru == 7:
                                f_list[i - 6] = s_pathsdg[7]
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                            elif count_tru >= 8:
                                f_list[i - 7] = s_pathsdg[8]
                                f_list[i - 6] = 'Non'
                                f_list[i - 5] = 'Non'
                                f_list[i - 4] = 'Non'
                                f_list[i - 3] = 'Non'
                                f_list[i - 2] = 'Non'
                                f_list[i - 1] = 'Non'
                                f_list[i] = 'Non'
                    else:
                        continue
                elif i == 0:
                    f_list[i] = s_pathsdg[1]
                elif a_listdg[i - 1] == 'Fal':
                    f_list[i] = s_pathsdg[1]
                else:
                    count_tru = 0
                    j = i
                    while j >= 0 and a_listdg[j] == 'Tru':
                        count_tru += 1
                        j -= 1
            
                    if count_tru == 1:
                        f_list[i] = s_pathsdg[1]
                    elif count_tru == 2:
                        f_list[i - 1] = s_pathsdg[2]
                        f_list[i] = 'Non'
                    elif count_tru == 3:
                        f_list[i - 2] = s_pathsdg[3]
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 4:
                        f_list[i - 3] = s_pathsdg[4]
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 5:
                        f_list[i - 4] = s_pathsdg[5]
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 6:
                        f_list[i - 5] = s_pathsdg[6]
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru == 7:
                        f_list[i - 6] = s_pathsdg[7]
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
                    elif count_tru >= 8:
                        f_list[i - 7] = s_pathsdg[8]
                        f_list[i - 6] = 'Non'
                        f_list[i - 5] = 'Non'
                        f_list[i - 4] = 'Non'
                        f_list[i - 3] = 'Non'
                        f_list[i - 2] = 'Non'
                        f_list[i - 1] = 'Non'
                        f_list[i] = 'Non'
            else:
                f_list[i] = s_paths[0]


        #ここからコード関連
        c_list = ['Fal'] * 64

        # 定義されているリストをまとめる
        paths_groups = [
            (s_pathsug, 'g'),
            (s_pathsugf, 'gf'),
            (s_pathsuf, 'f'),
            (s_pathsue, 'e'),
            (s_pathsuef, 'ef'),
            (s_pathsud, 'd'),
            (s_pathsudf, 'df'),
            (s_paths, 'c'),
            (s_pathsb, 'b'),
            (s_pathsbf, 'bf'),
            (s_pathsa, 'a'),
            (s_pathsaf, 'af'),
            (s_pathsg, 'g'),
            (s_pathsgf, 'gf'),
            (s_pathsf, 'f'),
            (s_pathse, 'e'),
            (s_pathsef, 'ef'),
            (s_pathsd, 'd'),
            (s_pathsdf, 'df'),
            (s_pathsc, 'c'),
            (s_pathsdb, 'b'),
            (s_pathsdbf, 'bf'),
            (s_pathsda, 'a'),
            (s_pathsdaf, 'af'),
            (s_pathsdg, 'g'),
        ]

        for i in range(len(f_list)):
            if f_list[i] == 'Non':
                c_list[i] = c_list[i-1]
            elif f_list[i] == s_paths[0]:
                c_list[i] = 'n'
            else:
                matched = False
                for paths, label in paths_groups:
                    if f_list[i] in paths[1:]:  # インデックス1以降の要素をチェック
                        c_list[i] = label
                        matched = True
                        break
                if not matched:
                    c_list[i] = 'default_value'  # 該当しない場合のデフォルト値を設定


        code_list = ['fa'] * 16
        kicode_list = ['fa'] * 16

        timestamps = time.perf_counter()

        #学習用csvデータ読み込み
        csvpath = os.path.join(settings.BASE_DIR, 'helloki', 'static', 'helloki', 'data', 'Bookki184.csv')

        csv = pd.read_csv(csvpath)

        self.params['datacsv'] = csv.head(3)

        xcol = ['b2','b1','m1','m2','m3','m4']

        tcol = ['code']

        

        X = csv[xcol]
        y = csv[tcol]


        one_hot_encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')


        X_encoded = one_hot_encoder.fit_transform(X)

# 訓練データとテストデータに分割
        X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)



# モデルのトレーニング
        model = tree.DecisionTreeClassifier(random_state=0)
        model.fit(X_train, y_train)

        c1_list = [c_list]

        kicode_list1 = [['n','n',c_list[0],c_list[1],c_list[2],c_list[3]]]
        kicode_list1_encoded = one_hot_encoder.transform(kicode_list1)

        kicode1 = model.predict(kicode_list1_encoded)

        kicode_list2 = [['n',kicode1[0],c_list[4],c_list[5],c_list[6],c_list[7]]]
        kicode_list2_encoded = one_hot_encoder.transform(kicode_list2)

        kicode2 = model.predict(kicode_list2_encoded)

        kicode_list3 = [[kicode1[0],kicode2[0],c_list[8],c_list[9],c_list[10],c_list[11]]]
        kicode_list3_encoded = one_hot_encoder.transform(kicode_list3)

        kicode3 = model.predict(kicode_list3_encoded)
        
        kicode_list4 = [[kicode2[0],kicode3[0],c_list[12],c_list[13],c_list[14],c_list[15]]]
        kicode_list4_encoded = one_hot_encoder.transform(kicode_list4)

        kicode4 = model.predict(kicode_list4_encoded)
        
        kicode_list5 = [[kicode3[0],kicode4[0],c_list[16],c_list[17],c_list[18],c_list[19]]]
        kicode_list5_encoded = one_hot_encoder.transform(kicode_list5)

        kicode5 = model.predict(kicode_list5_encoded)
        
        kicode_list6 = [[kicode4[0],kicode5[0],c_list[20],c_list[21],c_list[22],c_list[23]]]
        kicode_list6_encoded = one_hot_encoder.transform(kicode_list6)

        kicode6 = model.predict(kicode_list6_encoded)
        
        kicode_list7 = [[kicode5[0],kicode6[0],c_list[24],c_list[25],c_list[26],c_list[27]]]
        kicode_list7_encoded = one_hot_encoder.transform(kicode_list7)

        kicode7 = model.predict(kicode_list7_encoded)
        
        kicode_list8 = [[kicode6[0],kicode7[0],c_list[28],c_list[29],c_list[30],c_list[31]]]
        kicode_list8_encoded = one_hot_encoder.transform(kicode_list8)

        kicode8 = model.predict(kicode_list8_encoded)
        
        kicode_list9 = [[kicode7[0],kicode8[0],c_list[32],c_list[33],c_list[34],c_list[35]]]
        kicode_list9_encoded = one_hot_encoder.transform(kicode_list9)

        kicode9 = model.predict(kicode_list9_encoded)
        
        kicode_list10 = [[kicode8[0],kicode9[0],c_list[36],c_list[37],c_list[38],c_list[39]]]
        kicode_list10_encoded = one_hot_encoder.transform(kicode_list10)

        kicode10 = model.predict(kicode_list10_encoded)
        
        kicode_list11 = [[kicode9[0],kicode10[0],c_list[40],c_list[41],c_list[42],c_list[43]]]
        kicode_list11_encoded = one_hot_encoder.transform(kicode_list11)

        kicode11 = model.predict(kicode_list11_encoded)
        
        kicode_list12 = [[kicode10[0],kicode11[0],c_list[44],c_list[45],c_list[46],c_list[47]]]
        kicode_list12_encoded = one_hot_encoder.transform(kicode_list12)

        kicode12 = model.predict(kicode_list12_encoded)
        
        kicode_list13 = [[kicode11[0],kicode12[0],c_list[48],c_list[49],c_list[50],c_list[51]]]
        kicode_list13_encoded = one_hot_encoder.transform(kicode_list13)

        kicode13 = model.predict(kicode_list13_encoded)
        
        kicode_list14 = [[kicode12[0],kicode13[0],c_list[52],c_list[53],c_list[54],c_list[55]]]
        kicode_list14_encoded = one_hot_encoder.transform(kicode_list14)

        kicode14 = model.predict(kicode_list14_encoded)
        
        kicode_list15 = [[kicode13[0],kicode14[0],c_list[56],c_list[57],c_list[58],c_list[59]]]
        kicode_list15_encoded = one_hot_encoder.transform(kicode_list15)

        kicode15 = model.predict(kicode_list15_encoded)
        
        kicode_list16 = [[kicode14[0],kicode15[0],c_list[60],c_list[61],c_list[62],c_list[63]]]
        kicode_list16_encoded = one_hot_encoder.transform(kicode_list16)

        kicode16 = model.predict(kicode_list16_encoded)


        kicodelistf = [kicode1[0],kicode2[0],kicode3[0],kicode4[0],kicode5[0],kicode6[0],kicode7[0],kicode8[0],kicode9[0],kicode10[0],kicode11[0],kicode12[0],kicode13[0],kicode14[0],kicode15[0],kicode16[0]]

        timestampe = time.perf_counter()

        

        

        self.params['kicode'] = kicodelistf
    

        code_list1 = [c_list[0],c_list[1],c_list[2],c_list[3]]
        code_list2 = [c_list[4],c_list[5],c_list[6],c_list[7]]
        code_list3 = [c_list[8],c_list[9],c_list[10],c_list[11]]
        code_list4 = [c_list[12],c_list[13],c_list[14],c_list[15]]
        code_list5 = [c_list[16],c_list[17],c_list[18],c_list[19]]
        code_list6 = [c_list[20],c_list[21],c_list[22],c_list[23]]
        code_list7 = [c_list[24],c_list[25],c_list[26],c_list[27]]
        code_list8 = [c_list[28],c_list[29],c_list[30],c_list[31]]
        code_list9 = [c_list[32],c_list[33],c_list[34],c_list[35]]
        code_list10 = [c_list[36],c_list[37],c_list[38],c_list[39]]
        code_list11 = [c_list[40],c_list[41],c_list[42],c_list[43]]
        code_list12 = [c_list[44],c_list[45],c_list[46],c_list[47]]
        code_list13 = [c_list[48],c_list[49],c_list[50],c_list[51]]
        code_list14 = [c_list[52],c_list[53],c_list[54],c_list[55]]
        code_list15 = [c_list[56],c_list[57],c_list[58],c_list[59]]
        code_list16 = [c_list[60],c_list[61],c_list[62],c_list[63]]


        timestampas = time.perf_counter()


        def make_code(list,x):
            if list.count('c') + list.count('e') + list.count('g') == 4:
                code_list[x] = 'c'
            elif list.count('g') + list.count('b') + list.count('d') == 4:
                code_list[x] = 'g'
            elif list.count('a') + list.count('c') + list.count('e') == 4:
                if list.count('e') == 0 and x > 0 and code_list[x - 1] == 'am':
                    code_list[x] = 'f'
                else:
                    code_list[x] = 'am'
            elif list.count('e') + list.count('g') + list.count('b') == 4:
                code_list[x] = 'em'
            elif list.count('f') + list.count('a') + list.count('c') == 4:
                code_list[x] = 'f'
            elif list.count('d') + list.count('f') + list.count('a') == 4:
                code_list[x] = 'dm'
            elif list.count('e') > 2 and x == 0:
                code_list[x] = 'am'
            elif list.count('e') + list.count('b') > 2:
                code_list[x] = 'em'
            elif list.count('a') + list.count('c')== 3:
                if x > 0 and code_list[x - 1] == 'am':
                    code_list[x] = 'f'
                elif x > 1 and code_list[x-2] == 'am':
                    code_list[x] = 'f'
                else:
                    code_list[x] = 'am'
            elif list.count('c') + list.count('e') + list.count('g') == 3:
                code_list[x] = 'c'
            elif list.count('g') + list.count('b') + list.count('d') == 3:
                code_list[x] = 'g'
            elif list.count('a') + list.count('c') + list.count('e') == 3:
                if x > 0 and code_list[x - 1] == 'am':
                    code_list[x] = 'f'
                elif x > 1 and code_list[x-2] == 'am':
                    code_list[x] = 'f'
                else:
                    code_list[x] = 'am'
            elif list.count('e') + list.count('g') + list.count('b') == 3:
                code_list[x] = 'em'
            elif list.count('f') + list.count('a') + list.count('c') == 3:
                code_list[x] = 'f'
            elif list.count('d') + list.count('f') + list.count('a') == 3:
                code_list[x] = 'dm'
            elif list.count('af') > 0 and list.count('e') + list.count('b') >0:
                code_list[x] = 'e'
            elif list.count('gf') > 1:
                code_list[x] = 'e'
            elif list[0] == 'g' and list[1] == 'g' and list.count('c') == 0 and x > 0:
                code_list[x] = 'g'
            elif list.count('c') + list.count('e') + list.count('g') == 2:
                if list[0] == 'c' and list[2] != 'a':
                    code_list[x] = 'c'
                elif x == 0 :
                    code_list[x] = 'c'
                elif list[0] == 'e':
                    code_list[x] = 'c'
                elif list.count('d') + list.count('f') + list.count('a') > 1:
                    code_list[x] = 'dm'
                elif list.count('e') + list.count('g') + list.count('b') > 1:
                    code_list[x] = 'em'
                elif list.count('g') + list.count('b') + list.count('d') > 1:
                    code_list[x] = 'g'
                elif list.count('a') + list.count('c') + list.count('e') > 1:
                    code_list[x] = 'am'
                elif list.count('f') + list.count('a') + list.count('c') > 1:
                    code_list[x] = 'f'
                else:
                    code_list[x] = 'c'
            elif list.count('g') + list.count('b') + list.count('d') == 2:
                if list[0] == 'g':
                    code_list[x] = 'g'
                elif list[0] == 'b':
                    code_list[x] = 'g'
                elif list[0] == 'd':
                    code_list[x] = 'g'
                elif x > 0 and code_list[x - 1] == 'dm':
                    code_list[x] == 'g'
                elif list.count('a') + list.count('c') + list.count('e') > 1:
                    code_list[x] = 'am'
                elif list.count('d') + list.count('f') + list.count('a') > 1:
                    code_list[x] = 'dm'
                elif x > 0 and code_list[x - 1] == 'em':
                    code_list[x] = 'g'
                elif list.count('e') + list.count('g') + list.count('b') > 1:
                    code_list[x] = 'em'
                elif list.count('c') + list.count('e') + list.count('g') > 1:
                    code_list[x] = 'c'
                elif list.count('f') + list.count('a') + list.count('c') > 1:
                    code_list[x] = 'f'
                else:
                    code_list[x] = 'g'
            elif list.count('f') + list.count('a') + list.count('c') == 2:
                if list[0] == 'f':
                    code_list[x] = 'f'
                elif list.count('d') + list.count('f') + list.count('a') > 1:
                    code_list[x] = 'dm'
                elif list.count('e') + list.count('g') + list.count('b') > 1:
                    code_list[x] = 'em'
                elif list.count('g') + list.count('b') + list.count('d') > 1:
                    code_list[x] = 'g'
                elif list.count('a') + list.count('c') + list.count('e') > 1:
                    code_list[x] = 'am'
                elif list.count('c') + list.count('e') + list.count('g') > 1:
                    code_list[x] = 'c'
                else:
                    code_list[x] = 'f'
            elif list.count('a') + list.count('c') + list.count('e') == 2:
                if list[0] == 'a':
                    code_list[x] = 'am'
                elif list.count('d') + list.count('f') + list.count('a') > 1:
                    code_list[x] = 'dm'
                elif list.count('e') + list.count('g') + list.count('b') > 1:
                    code_list[x] = 'em'
                elif list.count('g') + list.count('b') + list.count('d') > 1:
                    code_list[x] = 'g'
                elif list.count('c') + list.count('e') + list.count('g') > 1:
                    code_list[x] = 'c'
                elif list.count('f') + list.count('a') + list.count('c') > 1:
                    code_list[x] = 'f'
                else:
                    code_list[x] = 'am'
            elif list.count('e') + list.count('g') + list.count('b') == 2:
                if list[0] == 'e':
                    code_list[x] = 'em'
                elif list.count('d') + list.count('f') + list.count('a') > 1:
                    code_list[x] = 'dm'
                elif list.count('c') + list.count('e') + list.count('g') > 1:
                    code_list[x] = 'c'
                elif list.count('g') + list.count('b') + list.count('d') > 1:
                    code_list[x] = 'g'
                elif list.count('a') + list.count('c') + list.count('e') > 1:
                    code_list[x] = 'am'
                elif list.count('f') + list.count('a') + list.count('c') > 1:
                    code_list[x] = 'f'
                else:
                    code_list[x] = 'em'
            elif list.count('d') + list.count('f') + list.count('a') == 2:
                if list[0] == 'd':
                    code_list[x] = 'dm'
                elif list.count('c') + list.count('e') + list.count('g') > 1:
                    code_list[x] = 'c'
                elif list.count('e') + list.count('g') + list.count('b') > 1:
                    code_list[x] = 'em'
                elif list.count('g') + list.count('b') + list.count('d') > 1:
                    code_list[x] = 'g'
                elif list.count('a') + list.count('c') + list.count('e') > 1:
                    code_list[x] = 'am'
                elif list.count('f') + list.count('a') + list.count('c') > 1:
                    code_list[x] = 'f'
                else:
                    code_list[x] = 'dm'
            elif list.count('af') >1:
                code_list[x] = 'e' 
            elif list.count('n') == 3:
                if list.count('c') > 0:
                    code_list[x] = 'c'
                elif list.count('b') > 0:
                    code_list[x] = 'g'
                elif list.count('a') > 0:
                    code_list[x] = 'am'
                elif list.count('g') > 0:
                    code_list[x] = 'g'
                elif list.count('f') > 0:
                    code_list[x] = 'f'
                elif list.count('e') > 0:
                    code_list[x] = 'em'
                elif list.count('d') > 0:
                    code_list[x] = 'dm'
                elif x > 0:
                    code_list[x] = code_list[x - 1]
                else:
                    code_list[x] = 'n'
            elif list.count('n') == 2:
                if list[0] == 'c':
                    code_list[x] = 'c'
                elif list[0] == 'b':
                    code_list[x] = 'g'
                elif list[0] == 'a':
                    code_list[x] = 'am'
                elif list[0] == 'g':
                    code_list[x] = 'g'
                elif list[0] == 'f':
                    code_list[x] = 'f'
                elif list[0] == 'e':
                    code_list[x] = 'em'
                elif list[0] == 'd':
                    code_list[x] = 'dm'
                elif list[1] == 'c':
                    code_list[x] = 'c'
                elif list[1] == 'b':
                    code_list[x] = 'g'
                elif list[1] == 'a':
                    code_list[x] = 'am'
                elif list[1] == 'g':
                    code_list[x] = 'g'
                elif list[1] == 'f':
                    code_list[x] = 'f'
                elif list[1] == 'e':
                    code_list[x] = 'em'
                elif list[1] == 'd':
                    code_list[x] = 'dm'
                elif list[2] == 'c':
                    code_list[x] = 'c'
                elif list[2] == 'b':
                    code_list[x] = 'g'
                elif list[2] == 'a':
                    code_list[x] = 'am'
                elif list[2] == 'g':
                    code_list[x] = 'g'
                elif list[2] == 'f':
                    code_list[x] = 'f'
                elif list[2] == 'e':
                    code_list[x] = 'em'
                elif list[2] == 'd':
                    code_list[x] = 'dm'
                else:
                    code_list[x] ='n'
            else:
                code_list[x] = 'n'
                

        make_code(code_list1,0)
        make_code(code_list2,1)
        make_code(code_list3,2)
        make_code(code_list4,3)
        make_code(code_list5,4)
        make_code(code_list6,5)
        make_code(code_list7,6)
        make_code(code_list8,7)
        make_code(code_list9,8)
        make_code(code_list10,9)
        make_code(code_list11,10)
        make_code(code_list12,11)
        make_code(code_list13,12)
        make_code(code_list14,13)
        make_code(code_list15,14)
        make_code(code_list16,15)

        timestampae = time.perf_counter()

        self.params['codename1'] = code_list[0]
        self.params['codename2'] = code_list[1]
        self.params['codename3'] = code_list[2]
        self.params['codename4'] = code_list[3]
        self.params['codename5'] = code_list[4]
        self.params['codename6'] = code_list[5]
        self.params['codename7'] = code_list[6]
        self.params['codename8'] = code_list[7]
        self.params['codename9'] = code_list[8]
        self.params['codename10'] = code_list[9]
        self.params['codename11'] = code_list[10]
        self.params['codename12'] = code_list[11]
        self.params['codename13'] = code_list[12]
        self.params['codename14'] = code_list[13]
        self.params['codename15'] = code_list[14]
        self.params['codename16'] = code_list[15]

        self.params['colist'] =c_list

        code_path = [
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'codec.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'codedm.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'codeem.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'codee.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'codef.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'codeg.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'codeam.mp3'),
            os.path.join(settings.BASE_DIR, 'hello', 'static', 'hello', 'audio', 'coden.mp3'),
        ]

        codepath_list = ['fa'] * 16

        for i in range(len(code_list)):
            if code_list[i] == 'c':
                codepath_list[i] = code_path[0]
            elif code_list[i] == 'dm':
                codepath_list[i] = code_path[1]
            elif code_list[i] == 'em':
                codepath_list[i] = code_path[2]
            elif code_list[i] == 'e':
                codepath_list[i] = code_path[3]
            elif code_list[i] == 'f':
                codepath_list[i] = code_path[4]
            elif code_list[i] == 'g':
                codepath_list[i] = code_path[5]
            elif code_list[i] == 'am':
                codepath_list[i] = code_path[6]
            elif code_list[i] == 'n':
                codepath_list[i] = code_path[7]
            else:
                codepath_list[i] = code_path[7]

        
        

        #ここまでコード関連


        # Noneを除去
        f_list = [item for item in f_list if item != 'Non']
        f_list = [item for item in f_list if item is not 'Non']

        timestamp = int(time.time())
        output_filename = f'sf_{timestamp}.mp3'
        output_path = os.path.join(settings.MEDIA_ROOT, output_filename)

        outputcode_filename = f'sfcode_{timestamp}.mp3'
        outputcode_path = os.path.join(settings.MEDIA_ROOT, outputcode_filename)

        outputfull_filename = f'sffull_{timestamp}.mp3'
        

        print("Output path:", output_path)  # 出力先パスをログに出力
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # 出力ファイルが存在する場合は削除
        if os.path.exists(output_path):
            os.remove(output_path)

        if os.path.exists(outputcode_path):
            os.remove(outputcode_path)

        inputs = [ffmpeg.input(audio) for audio in f_list]
        concatenated = ffmpeg.concat(*inputs, v=0, a=1).output(output_path)
        try:
            ffmpeg.run(concatenated, cmd='C:\\Users\\mirin\\Downloads\\ffmpeg-master-latest-win64-gpl-shared\\ffmpeg-master-latest-win64-gpl-shared\\bin\\ffmpeg.exe')
        except ffmpeg.Error as e:
            print(f"ffmpeg error occurred: {e.stderr}")

        #code
        inputscode = [ffmpeg.input(audio) for audio in codepath_list]
        concatenatedcode = ffmpeg.concat(*inputscode, v=0, a=1).output(outputcode_path)
        try:
            ffmpeg.run(concatenatedcode, cmd='C:\\Users\\mirin\\Downloads\\ffmpeg-master-latest-win64-gpl-shared\\ffmpeg-master-latest-win64-gpl-shared\\bin\\ffmpeg.exe')
        except ffmpeg.Error as e:
            print(f"ffmpeg error occurred: {e.stderr}")

        file1 = settings.MEDIA_URL + output_filename
        file2 = settings.MEDIA_URL + outputcode_filename
        outputc = settings.MEDIA_URL + outputfull_filename


        command = [
        'ffmpeg',
        '-i', file1,
        '-i', file2,
        '-filter_complex', 'amix=inputs=2:duration=first',
        '-c:a', 'mp3',
        outputc
        ]

        subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


        self.params['audio_url'] = settings.MEDIA_URL + output_filename
        self.params['audiocode_url'] = settings.MEDIA_URL + outputcode_filename
        self.params['audiofull_url'] = settings.MEDIA_URL + outputfull_filename
        self.params['form'] = HelloForm(request.POST)

        # 古い音声ファイルを削除
        old_files = glob.glob(os.path.join(settings.MEDIA_ROOT, 'sf_*.mp3'))
        for file in old_files:
            if file != output_path:
                os.remove(file)


        self.params['timea'] = timestampae - timestampas

        self.params['timek'] = timestampe - timestamps

        return render(request, 'helloki/indexki.html', self.params)
