import flet as ft
from compresser import main as compressor_main

input_path = ''

def main(page: ft.Page):
    page.window_width = 400        # window's width is 200 px
    page.window_height = 300       # window's height is 200 px
    page.update()
    
    def pick_files_result(e: ft.FilePickerResultEvent):
        global input_path
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelled!"
        )
        input_path = e.files[0].path
        selected_files.update()
    
    def button_clicked(e):
        boxes = [c.value for c in chechboxes]
        outpth = out_path.value
        if not outpth:
            outpth = 'compressed.pdf'
        elif not outpth.endswith('.pdf'):
            outpth += '.pdf'
        if not input_path:
            t.value = 'No input path'
            page.update()
        else:
            flag, ratio, size = compressor_main(input_path, outpth, remove=chechboxes[0].value)
            if flag:
                t.value = f'File compressed by {ratio:.2%}, final size is {size} MB.'
                page.update()
            else:
                t.value = ratio
                page.update()
    
    out_path = ft.TextField(label="Output path", value='compressed.pdf', width=400)
    page.add(out_path)
    
    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text()
    page.overlay.append(pick_files_dialog)

    page.add(
        ft.Row(
            [
                ft.ElevatedButton(
                    "Pick files",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: pick_files_dialog.pick_files(
                        allow_multiple=False
                    ),
                ),
                selected_files,
            ]
        )
    )
    
    chechboxes = [ft.Checkbox(label=cbox[0], value=cbox[1]) for cbox in (('Remove original file after compress', False),)]
    b = ft.ElevatedButton(text="Compress", on_click=button_clicked)
    page.add(*chechboxes, b)
    
    t = ft.Text()
    page.add(t)
    


ft.app(main)