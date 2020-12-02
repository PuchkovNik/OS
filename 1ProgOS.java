using System;
using System.IO;
using System.Text.Json;
using System.Xml;
namespace HelloApp
{
    class Num1
    {

        public string Name { get; set; }
        public int Age { get; set; }


        class Programm
        {
            static void Main(string[] args)
            {
                int vibor;
                bool end = true;
                while (end)
                {
                    Console.WriteLine(" \n1 \n2 \n3 \n4 \n5");
                    if (int.TryParse(Console.ReadLine(), out vibor) && (vibor > 0 && vibor < 6))
                    {


                        Console.Clear();
                        switch (vibor)
                        {
                            case 1:
                                DriveInfo[] drives = DriveInfo.GetDrives();

                                foreach (DriveInfo drive in drives)
                                {
                                    Console.WriteLine($"Название: {drive.Name}");
                                    Console.WriteLine($"Тип: {drive.DriveType}");
                                    Console.WriteLine($"Готов  ли диск :{drive.IsReady}");
                                    Console.WriteLine($"Обьём досткпного свободного места {drive.AvailableFreeSpace}");
                                    //Если диск готов то через идёт проверка для остаточной инфы.        
                                    if (drive.IsReady)
                                    {
                                        Console.WriteLine($"Объем диска: {drive.TotalSize}");
                                        Console.WriteLine($"Свободное пространство: {drive.TotalFreeSpace}");
                                        Console.WriteLine($"Метка: {drive.VolumeLabel}");
                                    }
                                }
                                break;
                            case 2:
                                string dirName = "C:\\";
                                if (Directory.Exists(dirName))
                                {
                                    Console.WriteLine("Подкатологи:");
                                    string[] dirs = Directory.GetDirectories(dirName);
                                    foreach (string s in dirs)
                                    {
                                        Console.Write($"|| {s} ||");
                                    }
                                    Console.WriteLine();
                                    Console.WriteLine("Файлы:");
                                    string[] files = Directory.GetFiles(dirName);
                                    foreach (string s in files)
                                    {
                                        Console.WriteLine($"|| {s} ||");
                                    }

                                }
                                Console.WriteLine("-------------");
                                break;
                            case 3:
                                Console.WriteLine("После записи файл будет немедленно удалён");
                                Console.WriteLine("Введите строку для записи в файл:");
                                // создаем каталог для файла
                                string path = @"C:\Пэпка";
                                DirectoryInfo dirInfo = new DirectoryInfo(path);
                                if (!dirInfo.Exists)
                                {
                                    dirInfo.Create();
                                }
                                string text = Console.ReadLine();
                                // запись в файл
                                using (FileStream fstream = new FileStream($@"{path}\текстовый файл.txt", FileMode.OpenOrCreate))
                                {
                                    // преобразуем строку в байты
                                    byte[] array = System.Text.Encoding.Default.GetBytes(text);
                                    // запись массива байтов в файл
                                    fstream.Write(array, 0, array.Length);
                                    Console.WriteLine("Текст записан в файл");
                                }
                                // чтение из файла
                                using (FileStream fstream = File.OpenRead($@"{path}\текстовый файл.txt"))
                                {
                                    // преобразуем строку в байты
                                    byte[] array = new byte[fstream.Length];
                                    // считываемданные
                                    fstream.Read(array, 0, array.Length);
                                    // декодируем байты в строку
                                    string textFromFile = System.Text.Encoding.Default.GetString(array);
                                    Console.WriteLine($"Текст из файла: {textFromFile}");
                                }
                                FileInfo fileInf = new FileInfo($@"{path}\текстовый файл.txt");
                                if (fileInf.Exists)
                                {
                                    File.Delete($@"{path}\текстовый файл.txt");
                                }
                                Console.WriteLine("Файл удалён");
                                break;
                            case 4:

                                Num1 tom = new Num1 { Name = "Tom", Age = 18 };
                                string json = JsonSerializer.Serialize<Num1>(tom);
                                Console.WriteLine(json);
                                Num1 restoredNum1 = JsonSerializer.Deserialize<Num1>(json);
                                Console.WriteLine(restoredNum1.Name);
                                Console.ReadLine();
                                break;
                            case 5:
                                XmlDocument xDoc = new XmlDocument();
                                xDoc.Load("C://users.xml");
                                // получим корневой элемент
                                XmlElement xRoot = xDoc.DocumentElement;
                                // обход всех узлов в корневом элементе
                                foreach (XmlNode xnode in xRoot)
                                {
                                    if (xnode.Attributes.Count > 0)
                                    {
                                        XmlNode attr = xnode.Attributes.GetNamedItem("name");
                                        if (attr != null)
                                            Console.WriteLine(attr.Value);
                                    }
                                    // обходим все дочерние узлы элемента user
                                    foreach (XmlNode childnode in xnode.ChildNodes)
                                    {
                                        // если узе л - company
                                        if (childnode.Name == "company")
                                        {
                                            Console.WriteLine($"Компания: {childnode.InnerText}");
                                        }
                                        // если узел age
                                        if (childnode.Name == "age")
                                        {
                                            Console.WriteLine($"Возраст: {childnode.InnerText}");
                                        }
                                    }
                                    Console.WriteLine();
                                }
                                Console.Read();
                                break;
                        }
                    }


                    else
                    {
                        Console.Clear();
                        Console.WriteLine("Неверны Ввод");
                        Console.WriteLine("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>");
                    }
                    Console.WriteLine("Выход");
                    Console.ReadKey();
                    Console.Clear();
                }
                Console.ReadLine();
                Console.ReadLine();

            }
        }
    }
}
