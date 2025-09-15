

from src.resume.domain.entities.resume import ResumeEntity


class IResumeGenerator:
    def generate(self, data: ResumeEntity) -> bytes:
        raise NotImplementedError