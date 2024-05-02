public class ConsoleOutControllee : IControllee
{
    public void DoSaveResult()
    {
        Console.WriteLine("SaveResult");
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