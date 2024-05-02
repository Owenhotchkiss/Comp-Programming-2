namespace pg273MassandWeight
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int mass = int.Parse(textBox1.Text);
            double newtons = mass * 9.8;
            if (newtons > 1000)
                label2.Text = "The object is too heavy";
            else if (newtons < 10)
                label2.Text = "The object is too light";
            else
                label2.Text = newtons.ToString();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}