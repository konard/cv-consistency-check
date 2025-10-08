export interface CVData {
  name?: string;
  position?: string;
  location?: string;
  skills?: string[];
  experience?: string[];
  education?: string[];
  // Add more fields as needed
}

export interface ComparisonResult {
  platform1: CVData;
  platform2: CVData;
  differences: {
    [key: string]: {
      value1: any;
      value2: any;
    };
  };
  matches: {
    [key: string]: any;
  };
}