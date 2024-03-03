from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.core.files import File
import subprocess

# Create your views here.
def index(request):
    return render(request, 'index.html')

# write, compile & return o/p
def compile_c_code(source_code):
    try:
        with open('Trail.h','w') as f:
            myfile = File(f) 
            myfile.write(source_code)
        source_file = "main.c"
        output_file = "main"
        try:
            result = subprocess.run(['gcc',source_file,'-o',output_file],stdout=subprocess.PIPE, stderr=subprocess.PIPE,check=True)
            if result.returncode == 0:
                pass
            else:
                raise subprocess.CalledProcessError(result.returncode, result.args, output=result.stdout, stderr=result.stderr)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"{e.stderr}")
        result = subprocess.run(['./' + output_file],capture_output=True,text=True)
        output = result.stdout
        return output
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Runtime ERROR:{e.stderr}")

def user_code(request):
    if request.method == 'POST':
        source_code = request.POST.get('code','')
        try:
            output = compile_c_code(source_code)
            output = output.strip()
            # messages.success(request,"Code compiled successfully")
            return render(request,'output.html',{'output': output})
        except Exception as e:
            messages.error(request,f"ERROR:{e}")
            return render(request,'index.html')
    else:
        return render(request,'index.html')
