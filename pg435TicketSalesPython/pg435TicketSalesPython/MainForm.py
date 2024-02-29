import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.MediumTurquoise
		self._button1.Location = System.Drawing.Point(86, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(137, 96)
		self._button1.TabIndex = 0
		self._button1.Text = "Student Form"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.MediumTurquoise
		self._button2.Location = System.Drawing.Point(86, 114)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(137, 91)
		self._button2.TabIndex = 1
		self._button2.Text = "Public Form"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightBlue
		self.ClientSize = System.Drawing.Size(301, 217)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "pg435TicketSalesPython"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		from frmStudent import *
		student = frmStudent(self)
		student.Show()
		self.Hide()

	def Button2Click(self, sender, e):
		from frmGeneral import *
		general = frmGeneral(self)
		general.Show()
		self.Hide()