from IPython.display import clear_output


import IPython
import uuid
import os

from google.colab import output

class InvokeButton(object):
  def __init__(self, title, callback):
    self._title = title
    self._callback = callback

  def _repr_html_(self):
    callback_id = 'button-' + str(uuid.uuid4())
    output.register_callback(callback_id, self._callback)

    template = """<div style='background-color:lightgreen'><h2>Provide your work here</h2><textarea id='d2345' style='width:500px;height:100px'></textarea>
        <br>
        <button id="{callback_id}">{title}</button>
        </div>
        <script>
          
          
          document.querySelector("#{callback_id}").onclick = (e) => {{
            var a = document.querySelector("#d2345").value;
            //console.log(a);
            google.colab.kernel.invokeFunction('{callback_id}', [a], {{}})
            e.preventDefault();
          }};
        </script>"""
    html = template.format(title=self._title, callback_id=callback_id)
    return html
  
def do_something(a):
  #clear_output()
  print(a)
  
  
  o=os.popen('pwd').read()
  print(o)
  #IMPORTANT: Pay attention quotation marks in a: https://stackoverflow.com/questions/17189237/how-can-i-write-and-append-using-echo-command-to-a-file
  
  display(IPython.display.HTML('<img src="/nbextensions/google.colab/example12345678.jpg" />'))
  
def main():
  clear_output()
  InvokeButton('click me', do_something)

if __name__ == "__main__":
    main()
