public class ConsoleOutControllee : IControllee
{
    public void DoAction2()
    {
        Console.WriteLine("Action2");
    }
    public void DoAction21()
    {
        Console.WriteLine("Action21");
    }
    public void DoAction31()
    {
        Console.WriteLine("Action31");
    }
    public void DoAction42()
    {
        Console.WriteLine("Action42");
    }
    public void DoAction421()
    {
        Console.WriteLine("Action421");
    }
    public void DoAction431()
    {
        Console.WriteLine("Action431");
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