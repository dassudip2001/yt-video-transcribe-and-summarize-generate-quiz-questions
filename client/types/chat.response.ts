export interface ChatResponse {
  summary: string;
  quiz: Quiz;
  quiz_raw: string;
  parse_error: any;
}

export interface Quiz {
  mcq: Mcq[];
  true_false: TrueFalse[];
  short_answer: ShortAnswer[];
}

export interface Mcq {
  question: string;
  options: string[];
  answer: string;
}

export interface TrueFalse {
  question: string;
  answer: boolean;
}

export interface ShortAnswer {
  question: string;
  answer: string;
}
