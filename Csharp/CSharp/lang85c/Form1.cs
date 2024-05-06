namespace lang85c
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num1 = int.Parse(textBox1.Text);
            int num2 = num1 - 165;
            double num3 = num2 / 100;
            int num4 = num2 / 100;
            label3.Text = (num4 + "/" + num3);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}