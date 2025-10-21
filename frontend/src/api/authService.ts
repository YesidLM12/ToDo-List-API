const API_URL = import.meta.env.VITE_API_URL;

export interface AuthResponse {
  access_token: string;
  token_type: string;
}

export interface UserCredentials {
  username: string;
  password: string;
}

export const login = async (
  credentials: UserCredentials
): Promise<AuthResponse> => {
  const res = await fetch(`${API_URL}/auth/login`, {
    method: "Post",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(credentials),
  });
  if (!res.ok) throw new Error("Invalid credentials");
  return res.json();
};

export const resgisterUser = async (
  credentials: UserCredentials
): Promise<any> => {
  const res = await fetch(`${API_URL}/auth/register`, {
    method: "Post",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(credentials),
  });
  if (!res.ok) throw new Error("Error registering user");
  return res.json();
};
