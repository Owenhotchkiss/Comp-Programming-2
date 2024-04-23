// See https://aka.ms/new-console-template for more information
Console.Write("Enter Weight: ");
int weight = int.Parse(Console.ReadLine());

Console.Write("Enter length: ");
int length = int.Parse(Console.ReadLine());

Console.Write("Enter width: ");
int width = int.Parse(Console.ReadLine());

Console.Write("Enter height: ");
int height = int.Parse(Console.ReadLine());

int volume = length * width * height;

if (weight > 27 && volume > 100_000);
    Console.WriteLine("Package is too heavy or too large");
else if (weight > 27)
    Console.WriteLine("Package is too heavy");
else if (volume > 100_000)
    Console.WriteLine("Package is okay");

Console.ReadLine();