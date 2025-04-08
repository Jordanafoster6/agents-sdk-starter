import { z } from 'zod';

export const AgentRequestSchema = z.object({
  input: z.string(),
  sessionId: z.string(),
});

export const AgentResponseSchema = z.object({
  output: z.string(),
  sessionId: z.string(),
});

export type AgentRequest = z.infer<typeof AgentRequestSchema>;
export type AgentResponse = z.infer<typeof AgentResponseSchema>;
