import tkinter as tk
import attend_info.ui_init as ui
import attend_info.make_widgets as widgets
import attend_info.info_dao as dao
import attend_info.info_service as service

if __name__ == '__main__':
    logo = 'logo.png'
    root = tk.Tk()
    app = ui.AppWindow(root, logo)
    dao = dao.InfoDao()
    service = service.InfoService(dao)
    widgets.make(app, service)
    app.mainloop()
