# SDK (Sofware Dataset kit)

## Agent:
The Agent class is the core configuration that defines an agent’s instructions, tools, and behavior.

## Instructions 
instruction is use to set a instuction it tell agent how it work developer set a instruction using string or callable function

## Handsoff
handsoff is used to handoff data one agent to another agent it mainly used when we work with multiple agents 

## Guardrails 
Guradil is used for checking the safety of response like someone say unethical or harmful or disrespect prompt so it make sure response is not harmful or voilent 

## Runner 
Runner main function is getting a response or sending a response it send from passing through a tools

## Run 
Run is class method  keeps the API clean and allows running without creating an instance.

## TContext
TContext represents the type of context or memory passed through the agent workflow.
