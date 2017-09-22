import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Calculattor")

        self.box = Gtk.Box(spacing=60)
        self.add(self.box)

        self.button1 = Gtk.Button(label="Daire")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Dikdörtgen")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

        self.button3 = Gtk.Button(label="")
        self.box.pack_start(self.button3, True, True, 0)

        self.text1 = Gtk.Entry()
        self.box.pack_start(self.text1, True, True, 0)

        self.text2 = Gtk.Entry()
        self.box.pack_start(self.text2, True, True, 0)

    def on_button1_clicked(self, widget):
        ik1 = self.text1.get_text()
        self.button3.set_label(" Dairenin alanı : {sonuc}".format(sonuc=self.daire_alan_hesapla_v2(int(ik1))))

    def on_button2_clicked(self, widget):
        ik1 = self.text1.get_text()
        ik2 = self.text2.get_text()
        self.button3.set_label("Dikdörtgenin alanı : {sonuc}".format(sonuc=self.dortgen_alan_hesapla_v2(int(ik1),int(ik2))))

    def dortgen_alan_hesapla_v2(self,k1,k2):
        if type(k1) == type(k2) == int:
            ka_ = k1 * k2
        else:
            ka_ = "Undefined"
        return ka_

    def daire_alan_hesapla_v2(self,r):
        if type(r) == int:
            ka_ = (r ** 2) * 3.14
        else:
            ka_ = "Undefined"
        return ka_




win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
