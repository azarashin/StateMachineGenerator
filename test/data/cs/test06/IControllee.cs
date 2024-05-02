public interface IControllee
{
    void DoSaveResult();
    void NoTransition(string state, string transition);
    void OverTransition(string transition);
}