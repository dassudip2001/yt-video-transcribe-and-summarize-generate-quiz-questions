"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import type { ChatResponse } from "@/types/chat.response";

export default function ChatMessage() {
  const [url, setUrl] = useState("");
  const [response, setResponse] = useState<ChatResponse | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  const handleGenerate = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setError("");
    setResponse(null);

    const trimmedUrl = url.trim();
    if (!trimmedUrl) {
      setError("Please paste a link before generating.");
      return;
    }

    try {
      setIsLoading(true);
      const res = await fetch("http://localhost:8000/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url: trimmedUrl }),
      });

      if (!res.ok) {
        const body = await res.text();
        throw new Error(body || `Server returned ${res.status}`);
      }

      const data: ChatResponse = await res.json();
      setResponse(data);
    } catch (err: any) {
      setError(err?.message ?? "Unable to generate summary.");
    } finally {
      setIsLoading(false);
    }
  };

  const handleReset = () => {
    setUrl("");
    setResponse(null);
    setError("");
  };

  return (
    <main className="min-h-screen bg-slate-50 py-10 px-4 text-slate-900">
      <div className="mx-auto w-full max-w-4xl rounded-3xl border border-slate-200 bg-white p-8 shadow-lg shadow-slate-200/20">
        <div className="space-y-3">
          <h1 className="text-3xl font-semibold">Link summary generator</h1>
          <p className="text-sm text-slate-600">
            Paste a video or article link and generate a summary plus quiz
            details.
          </p>
        </div>

        <form onSubmit={handleGenerate} className="mt-8 space-y-4">
          <label className="block">
            <span className="text-sm font-medium text-slate-700">
              Paste the link
            </span>
            <input
              value={url}
              onChange={(event) => setUrl(event.target.value)}
              placeholder="https://example.com/video-or-article"
              className="mt-2 w-full rounded-2xl border border-slate-300 bg-slate-50 px-4 py-3 text-sm text-slate-900 outline-none transition focus:border-slate-500 focus:ring-2 focus:ring-slate-200"
            />
          </label>

          <div className="flex flex-col gap-3 sm:flex-row sm:items-center">
            <Button
              type="submit"
              disabled={isLoading}
              className="min-w-[180px]"
            >
              {isLoading ? "Generating..." : "Generate summary"}
            </Button>
            <Button
              type="button"
              variant="outline"
              onClick={handleReset}
              disabled={isLoading}
            >
              Clear
            </Button>
          </div>

          {error ? (
            <div className="rounded-2xl border border-red-200 bg-red-50 p-4 text-sm text-red-700">
              {error}
            </div>
          ) : null}
        </form>

        {response ? (
          <section className="mt-8 space-y-6">
            <div className="rounded-3xl border border-slate-200 bg-slate-50 p-6">
              <h2 className="text-xl font-semibold text-slate-900">Summary</h2>
              <p className="mt-3 whitespace-pre-line text-slate-700">
                {response.summary || "No summary available."}
              </p>
            </div>

            {response.quiz ? (
              <div className="space-y-6">
                {response.quiz.mcq?.length ? (
                  <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
                    <h3 className="text-lg font-semibold">Multiple choice</h3>
                    <div className="mt-4 space-y-4">
                      {response.quiz.mcq.map((item, index) => (
                        <div
                          key={index}
                          className="rounded-2xl border border-slate-200 bg-slate-50 p-4"
                        >
                          <p className="font-medium text-slate-900">
                            {index + 1}. {item.question}
                          </p>
                          <ul className="mt-2 space-y-1 text-slate-700">
                            {item.options.map((option, optIndex) => (
                              <li key={optIndex} className="list-disc pl-5">
                                {option}
                              </li>
                            ))}
                          </ul>
                          <p className="mt-3 text-sm text-slate-600">
                            Answer: {item.answer}
                          </p>
                        </div>
                      ))}
                    </div>
                  </div>
                ) : null}

                {response.quiz.true_false?.length ? (
                  <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
                    <h3 className="text-lg font-semibold">True / False</h3>
                    <div className="mt-4 space-y-3 text-slate-700">
                      {response.quiz.true_false.map((item, index) => (
                        <div
                          key={index}
                          className="rounded-2xl border border-slate-200 bg-slate-50 p-4"
                        >
                          <p className="font-medium text-slate-900">
                            {index + 1}. {item.question}
                          </p>
                          <p className="mt-2 text-sm text-slate-600">
                            Answer: {item.answer ? "True" : "False"}
                          </p>
                        </div>
                      ))}
                    </div>
                  </div>
                ) : null}

                {response.quiz.short_answer?.length ? (
                  <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
                    <h3 className="text-lg font-semibold">Short answer</h3>
                    <div className="mt-4 space-y-3 text-slate-700">
                      {response.quiz.short_answer.map((item, index) => (
                        <div
                          key={index}
                          className="rounded-2xl border border-slate-200 bg-slate-50 p-4"
                        >
                          <p className="font-medium text-slate-900">
                            {index + 1}. {item.question}
                          </p>
                          <p className="mt-2 text-sm text-slate-600">
                            Answer: {item.answer}
                          </p>
                        </div>
                      ))}
                    </div>
                  </div>
                ) : null}
              </div>
            ) : null}

            {response.quiz_raw ? (
              <div className="rounded-3xl border border-slate-200 bg-slate-50 p-6">
                <h3 className="text-lg font-semibold">Raw quiz output</h3>
                <pre className="mt-3 max-h-72 overflow-auto whitespace-pre-wrap text-sm text-slate-700">
                  {response.quiz_raw}
                </pre>
              </div>
            ) : null}

            {response.parse_error ? (
              <div className="rounded-3xl border border-amber-200 bg-amber-50 p-6 text-slate-700">
                <h3 className="text-lg font-semibold text-amber-900">
                  Parse error
                </h3>
                <p className="mt-2 text-sm">{response.parse_error}</p>
              </div>
            ) : null}
          </section>
        ) : null}
      </div>
    </main>
  );
}
