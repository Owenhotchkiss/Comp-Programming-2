namespace pg273BookClubPoints
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            label3.Text = "";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int points = 0;
            int books = int.Parse(textBox1.Text);
            if (books == 0)
                points = 0;
            else if (books == 1)
                points = 1;
            else if (books == 2)
                points = 15;
            else if (books == 3)
                points = 30;
            else if( books >= 4)
                points = 60;
            label3.Text = points.ToString();
        }
    }
}