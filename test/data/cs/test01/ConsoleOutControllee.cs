public class ConsoleOutControllee : IControllee
{
    public void DoAction1()
    {
        Console.WriteLine("Action1");
    }
    public void DoAction2()
    {
        Console.WriteLine("Action2");
    }
    public void DoAction3()
    {
        Console.WriteLine("Action3");
    }
    public void NoTransition(string state, string transition)
    {
        Console.WriteLine($"NoTransition({state}: {transition})");
    }
    public void OverTransition(string transition)
    {
        Console.WriteLine($"OverTransition({transition})");
    }
}